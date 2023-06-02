import requests, json

url = "http://alchemestry.python-newbie.net/"
html = requests.get(url).text

temp = json.loads(html)
isp = temp['data']['isp']
jam = temp['data']['timezone']
provinsi = temp['data']['regionName']
negara = temp['data']['country']
kota = temp['data']['city']
lat = temp['data']['lat']
query = temp['data']['query']
print(f"ISP : {isp}\nNegara : {negara}\nProvinsi : {provinsi}\nKota : {kota}\nTimezone : {jam}")
print(temp)
print(lat)
print(query)