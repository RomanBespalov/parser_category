from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def check_ip():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5://72.206.181.97:64943',
        'https': 'socks5://72.206.181.97:64943',
    }
    session.verify = False
    html = session.get('https://www.okeydostavka.ru/').text
    soup = BeautifulSoup(html, 'lxml')
    ip_address = soup.find(class_='ip').text.strip()

    return f'IP: {ip_address}'


print(check_ip())
