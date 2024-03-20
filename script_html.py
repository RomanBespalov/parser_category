import logging
import sys
import time

import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager


#  Сайт магазина:
URL = 'https://www.okeydostavka.ru/'

# Прокси сервер:
PROXY = 'socks5://72.206.181.97:64943'

# Выберите адрес доставки:
DELIVERY_ADDRESS = 'Москва, улица Вилиса Лациса, 18'


class Parse():
    """Класс Парсер, создает настройки для браузера."""

    def __init__(self, proxy):
        """Функция создания и настройки драйвера."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--proxy-server=%s' % proxy)
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self.wait = WebDriverWait(self.driver, 30)
        stealth(
            self.driver,
            languages=['en-US', 'en'],
            vendor='Google Inc.',
            platform='Win32',
            webgl_vendor='Intel Inc.',
            renderer='Intel Iris OpenGL Engine',
            fix_hairline=True,
        )

    def parse_category(self, url, delivery_adress):
        """Функция для парсинга данных."""
        self.driver.get(url)

        # Подтверждение использование Куки
        try:
            cookie_alert_xpath = '//*[@id="cookie_alert"]/div/div[2]/button'
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, cookie_alert_xpath))
            )
            self.driver.find_element(By.XPATH, cookie_alert_xpath).click()
            time.sleep(1)
        except TimeoutException:
            logging.info(
                'Элемент Куки не найден в течение '
                'отведенного времени или отсутствует'
            )

        # Клик на кнопку выбора адреса доставки
        delivery_adress_xpath = '//*[@id="availableReceiptTimeslot"]'
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, delivery_adress_xpath))
        )
        element.click()

        # Ввод данных адреса доставки
        search_input_xpath = '//*[@id="addressSelectionQuery"]'
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, search_input_xpath))
        )
        search_input = self.driver.find_element('xpath', search_input_xpath)
        search_input.send_keys(delivery_adress)
        save_button_xpath = '//*[@id="addressSelectionButton"]'
        self.driver.find_element('xpath', save_button_xpath).click()
        time.sleep(1)
        own_bakery_xpath = '//*[@id="departmentLink_3074457345616852723_alt"]'
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, own_bakery_xpath))
        )
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, own_bakery_xpath))
        )
        self.driver.find_element(By.XPATH, own_bakery_xpath).click()

        # Парсинг товаров из категории
        shop_adress_xpath = (
            '//*[@id="citySelectionLink"]/tbody/tr/td[1]/div[1]/span'
        )
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, shop_adress_xpath))
        )
        shop_adress = self.driver.find_element(
            By.XPATH, shop_adress_xpath
        ).text

        def cycle():
            category_name_xpath = (
                '//*[@id="PageHeading_4_-1001_3074457345618259710"]/h1'
            )
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, category_name_xpath))
            )
            category_name = self.driver.find_element(
                By.XPATH, category_name_xpath
            ).text
            products_container = self.wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'product_listing_container')
                )
            )
            product_elements = products_container.find_elements(
                By.CLASS_NAME, 'product'
            )

            for product_element in product_elements:
                product_name = product_element.find_element(
                    By.CLASS_NAME, 'product-name'
                ).text
                list_price_elements = product_element.find_elements(
                    By.CLASS_NAME, 'price.label'
                )
                offer_price_elements = product_element.find_elements(
                    By.CLASS_NAME, 'label.crossed'
                )
                product_link_element = product_element.find_element(
                    By.TAG_NAME, 'a'
                )
                product_url = product_link_element.get_attribute('href')

                image_element = product_element.find_element(
                    By.CSS_SELECTOR, 'div.image > a > img'
                )

                # Получаем URL изображения
                image_url = image_element.get_attribute('data-src')
                base_url = "https://www.okeydostavka.ru/"
                image_url = base_url + image_url

                for price_element in offer_price_elements:
                    price_text = price_element.text
                    if price_text == '':
                        old_prices = []
                        continue
                    old_prices = ' '.join(price_text.split()[:-1])

                for price_element in list_price_elements:
                    price_text = price_element.text
                    if price_text == '':
                        prices = []
                        continue
                    prices = ' '.join(price_text.split()[:-1])

                product_info = {
                    'адрес магазина': shop_adress,
                    'категория товара': category_name,
                    'url товара': product_url,
                    'наименование товара': product_name,
                    'ссылка на изображение товара': image_url,
                    'цена': prices,
                    'цена без учета скидки': old_prices,
                }
                if len(product_info['цена без учета скидки']) == 0:
                    product_info.pop('цена без учета скидки', None)

                file_path = "output.txt"
                with open(file_path, "a", encoding="utf-8") as file:
                    file.write(
                        json.dumps(product_info, ensure_ascii=False) + "\n"
                    )

        cycle()

        # Переход на главную страницу
        main_menu_xpath = (
            '//*[@id="WC_BreadCrumb_Link_1_1_-1028_3074457345618259705"]/span'
        )
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, main_menu_xpath))
        )
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, main_menu_xpath))
        )
        self.driver.find_element(By.XPATH, main_menu_xpath).click()

        # Готовая кулинария
        cooking_xpath = (
            '//*[@id="departmentLink_3074457345616852722_alt"]/div/div[1]'
        )
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, cooking_xpath))
        )
        self.wait.until(EC.element_to_be_clickable((By.XPATH, cooking_xpath)))
        self.driver.find_element(By.XPATH, cooking_xpath).click()
        cycle()

        # Переход на главную страницу
        main_menu_xpath = (
            '//*[@id="WC_BreadCrumb_Link_1_1_-1028_3074457345618259705"]/span'
        )
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, main_menu_xpath))
        )
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, main_menu_xpath))
        )
        self.driver.find_element(By.XPATH, main_menu_xpath).click()

        # Мясо, птица, колбасы
        food_xpath = '//*[@id="departmentLink_16551_alt"]/div/div[1]'
        self.wait.until(EC.presence_of_element_located((By.XPATH, food_xpath)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, food_xpath)))
        self.driver.find_element(By.XPATH, food_xpath).click()

        # Мясо
        meat_xpath = ('//*[@id="container_3074457345618268756"]'
                      '/div[3]/div[2]/div[1]/div[2]/div[1]/h2/a'
                      )
        self.wait.until(EC.presence_of_element_located((By.XPATH, meat_xpath)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, meat_xpath)))
        self.driver.find_element(By.XPATH, meat_xpath).click()
        cycle()


def main():
    parse_driver = Parse(PROXY)
    parse_driver.parse_category(URL, DELIVERY_ADDRESS)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
