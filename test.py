# import requests

# url = "https://www.dns-shop.ru/catalog/17aa734716404e77/vstraivaemye-morozilnye-shkafy/"

# headers = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#   'Accept-Language': 'ru-RU,ru;q=0.9',
#   'Cache-Control': 'max-age=0',
#   'Connection': 'keep-alive',
#   'Cookie': 'qrator_jsr=1709302365.751.PVfYQkh9QpmxLMxg-nq7e4akdn7uhvjibglruoc4ep0bbs424-00; qrator_ssid=1709302366.591.L0zhSUemjpfY34xF-12du46n0bu7njo7nf11gvbl0r10rti1s; qrator_jsid=1709302365.751.PVfYQkh9QpmxLMxg-n8npgiin2imdhk0anhqu89l489juepoe; _ab_=%7B%22aaa-test%22%3A%22GROUP_AAA_1%22%7D; city_path=moscow; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; lang=ru; qrator_jsr=1709302276.856.PtWzSJJqhEf9BJ0T-co383e8nmgb6joda11ftcrhkg0f1l1i9-00; qrator_ssid=1709301319.151.3e4BWq1XDr9Lu5L4-gok9qfio4tk9dokno9nll3kt6vs24epa; PHPSESSID=9a58d97ce9d96a4373b87fd7bc5ed762; _csrf=b15a88b10ae33272cc3ac514bf8cdfec8a4d04c79cfad8269fa0133b4b98043fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222RrpxMXLf37uuzq__FtSrjHqXvWi_wm8%22%3B%7D',
#   'Sec-Fetch-Dest': 'document',
#   'Sec-Fetch-Mode': 'navigate',
#   'Sec-Fetch-Site': 'same-origin',
#   'Upgrade-Insecure-Requests': '1',
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
#   'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"macOS"'
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

import requests

url = "https://www.dns-shop.ru/ajax-state/product-buy/"

payload = 'data=%7B%22type%22%3A%22product-buy%22%2C%22containers%22%3A%5B%7B%22id%22%3A%22as-kTK4S1%22%2C%22data%22%3A%7B%22id%22%3A%225046616%22%7D%7D%2C%7B%22id%22%3A%22as-vnITjL%22%2C%22data%22%3A%7B%22id%22%3A%228198415%22%7D%7D%2C%7B%22id%22%3A%22as-t6o3Zi%22%2C%22data%22%3A%7B%22id%22%3A%225355335%22%7D%7D%2C%7B%22id%22%3A%22as-OG5IuO%22%2C%22data%22%3A%7B%22id%22%3A%226617352%22%7D%7D%2C%7B%22id%22%3A%22as-Na3gw8%22%2C%22data%22%3A%7B%22id%22%3A%228112168%22%7D%7D%2C%7B%22id%22%3A%22as-vfU7F4%22%2C%22data%22%3A%7B%22id%22%3A%228157655%22%7D%7D%2C%7B%22id%22%3A%22as-VbFOs2%22%2C%22data%22%3A%7B%22id%22%3A%229959790%22%7D%7D%2C%7B%22id%22%3A%22as-OcqHGl%22%2C%22data%22%3A%7B%22id%22%3A%228130240%22%7D%7D%2C%7B%22id%22%3A%22as-BRYPL6%22%2C%22data%22%3A%7B%22id%22%3A%228198416%22%7D%7D%2C%7B%22id%22%3A%22as-_miHa8%22%2C%22data%22%3A%7B%22id%22%3A%229007163%22%7D%7D%2C%7B%22id%22%3A%22as-hrmi-5%22%2C%22data%22%3A%7B%22id%22%3A%225043546%22%7D%7D%2C%7B%22id%22%3A%22as-roJydH%22%2C%22data%22%3A%7B%22id%22%3A%229959788%22%7D%7D%2C%7B%22id%22%3A%22as-dkWOpx%22%2C%22data%22%3A%7B%22id%22%3A%225427582%22%7D%7D%2C%7B%22id%22%3A%22as-tkWbMf%22%2C%22data%22%3A%7B%22id%22%3A%225043561%22%7D%7D%2C%7B%22id%22%3A%22as-KowK20%22%2C%22data%22%3A%7B%22id%22%3A%225077934%22%7D%7D%5D%7D'
headers = {
  'Accept': '*/*',
  'Accept-Language': 'ru-RU,ru;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'qrator_ssid=1709302366.591.L0zhSUemjpfY34xF-12du46n0bu7njo7nf11gvbl0r10rti1s; qrator_jsid=1709302365.751.PVfYQkh9QpmxLMxg-n8npgiin2imdhk0anhqu89l489juepoe; lang=ru; city_path=moscow; _ab_=%7B%22aaa-test%22%3A%22GROUP_AAA_2%22%7D; PHPSESSID=c6273df4ad0b5961511e8aef56310334; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; _csrf=9f490f092b7b6d0da098594322f28423ad9c61c213cd071436bf7bfb8b5c9311a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%224rA5ggbyC9qwjAqk9U75AJAcfO2DjWGB%22%3B%7D; rrpvid=944067940613632; _gid=GA1.2.268503386.1709302368; phonesIdentV2=56f0c0e4-07c3-47b1-a9f1-bfe25b5c3203; rcuid=65e1e260ad37ec1bf5d4240b; cartUserCookieIdent_v3=27ff29c671d46d30881095dd8427e38974bf9a0dc9c53b9c4f12ed145caccc9da%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22ceca9a89-5cf2-3eb2-a08f-1c0efb975ac6%22%3B%7D; _gcl_au=1.1.1377772794.1709302370; tmr_lvid=5dcab8e5580fda56d30861051abc039d; tmr_lvidTS=1709302370018; qrator_msid=1709302370.082.JvSsDZRYBfOBbEap-9ajvtr55ctfb7e8hlh1u9q3fj1bkeqp5; _ym_uid=1709302371303443132; _ym_d=1709302371; _ym_isad=2; _ym_visorc=b; adrdel=1; adrcid=AIa_kpQqScjmZiba4o_KgTA; tmr_detect=0%7C1709302608618; _ga=GA1.1.613670531.1709302368; _ga_FLS4JETDHW=GS1.1.1709302369.1.1.1709302698.29.0.253921759; _gat=1; rr-testCookie=testvalue; _ab_=%7B%22aaa-test%22%3A%22GROUP_AAA_1%22%7D; city_path=moscow; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; lang=ru; qrator_jsid=1709302365.751.PVfYQkh9QpmxLMxg-ml18qr5psi7o6kuost292ac411mu67if; qrator_ssid=1709301319.151.3e4BWq1XDr9Lu5L4-gok9qfio4tk9dokno9nll3kt6vs24epa; PHPSESSID=9a58d97ce9d96a4373b87fd7bc5ed762; _csrf=b15a88b10ae33272cc3ac514bf8cdfec8a4d04c79cfad8269fa0133b4b98043fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222RrpxMXLf37uuzq__FtSrjHqXvWi_wm8%22%3B%7D',
  'Origin': 'https://www.dns-shop.ru',
  'Referer': 'https://www.dns-shop.ru/catalog/17aa734716404e77/vstraivaemye-morozilnye-shkafy/no-referrer',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
  'X-CSRF-Token': 'b7AeHfxmpMWkcam1EahCDm7C7XU9Y7u9dxKK3DXZcllbwl8omwHGvOdI2MJ76TNlV5faQHwp-t4RXbiYX441Gw==',
  'X-Requested-With': 'XMLHttpRequest',
  'content-type': 'application/x-www-form-urlencoded',
  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()
print(data['data']['states'][0]['data']['price']['current'])
