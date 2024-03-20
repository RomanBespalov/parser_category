import requests
import json

url = "https://www.okeydostavka.ru/wcs/resources/mobihub023/store/13151/catalog/product/prices"

payload = json.dumps({
  "ids": [
    "26589",
    "26894",
    "37576",
    "39660",
    "954756",
    "487390",
    "503631",
    "3074457345617768497",
    "3074457345617777303",
    "3074457345617777306",
    "790007",
    "3074457345617789382",
    "3074457345617856797",
    "3074457345617876171",
    "3074457345617876188"
  ]
})
headers = {
  'authority': 'www.okeydostavka.ru',
  'accept': 'application/javascript, application/json',
  'accept-language': 'ru,en;q=0.9',
  'cache-control': 'max-age=0',
  'channel': '-1',
  'content-language': 'ru-RU',
  'content-type': 'application/json',
  'cookie': 'spid=1709231215236_1840b620462e2c331e92d179bb3ae941_kwwi4598ubhg9dqd; JSESSIONID=0000Fnd6foq1VEkNuDNHltc1vBv:-1; storeGroup=msk1; ffcId=13151; WC_SESSION_ESTABLISHED=true; WC_AUTHENTICATION_-1002=-1002%2CzZHlyRjQcgWKqNcfDjyX4iZ02zjcQoyDurbFiQxFNVk%3D; WC_ACTIVEPOINTER=-20%2C10151; WC_USERACTIVITY_-1002=-1002%2C10151%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1877362032%2Cver_null%2Ci61YGk29VOLyWRQAULrYPENqJXlyIKfg5eQyZpUGqJG55OrQaZeEgifPoNV9Ez3%2F8lVG0rBcYFDHrsAfIfnUZ0nnsoG32L%2B4pzbNxPZH%2BdVbFHk908VgSXYnc%2F7IRcMakGBZ9gi1V0ty0aCK0cf4mu7c0Jm2WFt4CTGmAPzZtGnTZ4kDeYcyu7r%2B85%2Fwere1dxHgfxkCr0frMJ5Zy1rxUPTQh%2BX%2FVVz86K%2BIhI0TlGyu4e6JYKNIeKr%2BtdOca%2Fmb; WC_GENERIC_ACTIVITYDATA=[7200145342%3Atrue%3Afalse%3A0%3AkmME9USydbAUkMKyA2M%2BSR1B%2FOpFsFYNahoEhmzUVHk%3D][com.ibm.commerce.context.entitlement.EntitlementContext|4000000000000000003%264000000000000000003%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|null][com.ibm.commerce.context.globalization.GlobalizationContext|-20%26RUB%26-20%26RUB][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10551%26null%26false%26false%26false][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.ibm.commerce.context.bcsversion.BusinessContextVersionContext|null][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10151%26-1002%26-1002%26-1][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null]; solarfri=779b98c38dcafd5e; _ga=GA1.1.1972488693.1709231216; _ym_uid=1709231216839925258; _ym_d=1709231216; isNative=1; _ym_isad=2; selectedCity=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; acceptCookie=1; spsc=1709231525609_87608914e7739869222e4cb5faa3beaa_2dc4c47e5beb4aae25be080fa9d16c8093e7e989cef732b63b8bada59af3d7da; selectedStore=10151_13151; gtmListKey=GTM_LIST_CATALOG; _ga_VBYWB70QLD=GS1.1.1709231216.1.1.1709232659.59.0.0',
  'if-none-match': '*',
  'origin': 'https://www.okeydostavka.ru',
  'referer': 'https://www.okeydostavka.ru/msk/%D1%81%D0%B2%D0%BE%D1%8F-%D0%BF%D0%B5%D0%BA%D0%B0%D1%80%D0%BD%D1%8F',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
response_2 = requests.get('https://www.okeydostavka.ru/msk/своя-пекарня', headers=headers)
print(response_2.text)

# import requests

# url = 'https://mc.yandex.ru/watch/27891822/1?page-url=https%3A%2F%2Fwww.okeydostavka.ru%2Fmsk%2F%25D1%2581%25D0%25B2%25D0%25BE%25D1%258F-%25D0%25BF%25D0%25B5%25D0%25BA%25D0%25B0%25D1%2580%25D0%25BD%25D1%258F&charset=utf-8&uah=chu%0A%22Not_A%20Brand%22%3Bv%3D%228%22%2C%22Chromium%22%3Bv%3D%22120%22%2C%22YaBrowser%22%3Bv%3D%2224.1%22%2C%22Yowser%22%3Bv%3D%222.5%22%0Acha%0Aarm%0Achb%0A64%0Achf%0A24.1.1.911%0Achl%0A%22Not_A%20Brand%22%3Bv%3D%228.0.0.0%22%2C%22Chromium%22%3Bv%3D%22120.0.6099.234%22%2C%22YaBrowser%22%3Bv%3D%2224.1.1.911%22%2C%22Yowser%22%3Bv%3D%222.5%22%0Achm%0A%3F0%0Achp%0AmacOS%0Achv%0A14.3.1&hittoken=1709237002_567a3d8d29ac84afde5145c22c91c6b9f302deef4ead7f0bcceae102ff5327fb&browser-info=pa%3A1%3Aar%3A1%3Avf%3Aqfujqr3o4ekpu96fyam058f3%3Afu%3A1%3Aen%3Autf-8%3Ala%3Aru%3Av%3A1251%3Acn%3A1%3Adp%3A0%3Als%3A1663232057872%3Ahid%3A295113501%3Az%3A240%3Ai%3A20240301000322%3Aet%3A1709237003%3Ac%3A1%3Arn%3A236914707%3Arqn%3A84%3Au%3A1709231216839925258%3Aw%3A1440x400%3As%3A1440x900x30%3Ask%3A2%3Awv%3A2%3Ads%3A%2C%2C%2C%2C%2C%2C%2C%2C%2C1186%2C1186%2C23%2C%3Aco%3A0%3Acpf%3A1%3Aeu%3A0%3Ans%3A1709237001138%3Agi%3AR0ExLjEuMTk3MjQ4ODY5My4xNzA5MjMxMjE2%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1709237003&t=gdpr(14)clc(0-0-0)rqnt(2)lt(56800)aw(1)rcm(0)ecs(0)cdl(na)ti(1)'

# headers = {
#     'authority': 'mc.yandex.ru',
#     'accept': '*/*',
#     'accept-language': 'ru,en;q=0.9',
#     'content-type': 'application/x-www-form-urlencoded',
#     'cookie': 'ваш_cookie_здесь',
#     'origin': 'https://www.okeydostavka.ru',
#     'referer': 'https://www.okeydostavka.ru/',
#     'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': 'macOS',
#     'sec-ch-ua-version': '"14.3.1"',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
# }

# response = requests.get(url, headers=headers)

# print(response.text)
