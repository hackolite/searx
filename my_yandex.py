import requests
url = "https://yandex.com/search/xml?user=uid-cru23u4o&key=03.611919183:46f4e2421e8a9964a50a703bd2201eb7&query=martinique tourisme&l10n=en&sortby=tm.order%3Dascending&filter=strict&groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D10.docs-in-group%3D1"

resp = requests.get(url)
print(resp.text)
