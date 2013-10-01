# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from crawler.items import Affair
from crawler.loaders import AffairLoader


class CuriaVistaSpider(CrawlSpider):
    name = 'curia_vista'
    allowed_domains = ['parlament.ch']
    start_urls = [
        # Start by searching for an empty string.
        'http://www.parlament.ch/d/suche/Seiten/resultate.aspx?collection=CV' +
            '&gvk_gtyp_key=1,2,3,4,5,6,7,8,9,10,12,13,14,18,19&sort=GN&way=desc',
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=('resultate\.aspx',))),
        Rule(SgmlLinkExtractor(allow=('geschaefte\.aspx',)), callback='parse_item'),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        l = AffairLoader(item=Affair(), selector=hxs.select('//div[@id="content"]'))
        l.add_xpath('title', './/h3[@class="cv-title"]/text()')
        l.add_xpath('number', './/h2[@class="cv-title"]', re=ur'>(\d+\.\d+) \u2013')
        l.add_xpath('issue_type', './/h2[@class="cv-title"]', re=ur'\u2013 (.*)</h2>')
        l.add_xpath('issued_by', './/ul[@class="profilelist small"]//span/text()')
        l.add_xpath('issue_date',
                './/dt[text()="Einreichungsdatum"]/following-sibling::dd[1]/text()')
        l.add_xpath('status',
                './/dt[text()="Stand der Beratung"]/following-sibling::dd[1]/text()')
        l.add_xpath('content',
                './div[@class="contentelementfull"][2]/div[@class="contentelement"]//text()')
        l.add_value('url', response.url)
        return l.load_item()
