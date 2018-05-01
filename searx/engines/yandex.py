"""
 Yahoo (Web)

 @website     https://yandex.ru/
 @provide-api ?
 @using-api   no
 @results     HTML (using search portal)
 @stable      no (HTML can change)
 @parse       url, title, content
"""

from lxml import html
from searx import logger
from searx.url_utils import urlencode




import requests

logger = logger.getChild('yandex engine')

# engine dependent config
categories = ['general']
paging = True
language_support = True  # TODO

default_tld = 'com'
language_map = {'ru': 'ru',
                'ua': 'ua',
                'be': 'by',
                'kk': 'kz',
                'tr': 'com.tr'}

# search-url
base_url = 'https://yandex.{tld}/'
search_url = 'search/?{query}&p={page}'

results_xpath = '//li[@class="serp-item"]'
url_xpath = './/h2/a/@href'
title_xpath = './/h2/a//text()'
content_xpath = './/div[@class="text-container typo typo_text_m typo_line_m organic__text"]//text()'


def request(query, params):
    lang = params['language'].split('-')[0]
    host = base_url.format(tld=language_map.get(lang) or default_tld)
    params['url'] = host + search_url.format(page=params['pageno'] - 1,
                                             query=urlencode({'text': query}))
    #print(params)
    #params['url'] = "https://yandex.com/search/xml?user=uid-cru23u4o&key=03.611919183:46f4e2421e8a9964a50a703bd2201eb7&l10n=en&sortby=tm.order%3Dascending&filter=strict&groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D10.docs-in-group%3D1"
    return params


# get response from search-request
def response(resp):
    logger.debug(resp.text)
    dom = html.fromstring(resp.text)
    results = []
    for result in dom.xpath(results_xpath):
        try:
            res = {'url': result.xpath(url_xpath)[0],
                   'title': ''.join(result.xpath(title_xpath)),
                   'content': ''.join(result.xpath(content_xpath))}
        except:
            logger.exception('yandex parse crash')
            continue
        results.append(res)

    return results
