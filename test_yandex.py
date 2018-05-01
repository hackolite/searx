# importing the requests library
import requests

payload ="""<?xml version="1.0" encoding="utf-8"?>
<request>
  <query>
    emploi martinique
  </query>
  <groupings>
    <groupby attr="d" mode="deep" groups-on-page="10" docs-in-group="1" />
  </groupings>
</request>"""


# api-endpoint
URL = "https://yandex.com/search/xml?user=uid-cru23u4o&key=03.611919183:46f4e2421e8a9964a50a703bd2201eb7&l10n=fr&filter=strict"
# sending get request and saving the response as response object
r = requests.post(url = URL, data = payload)
print(r.text)
