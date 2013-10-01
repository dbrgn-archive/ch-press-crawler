# -*- coding: utf-8 -*-
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Join, Compose


def stripper(text):
    return text.strip()


class AffairLoader(XPathItemLoader):
    default_output_processor = Compose(TakeFirst(), stripper)
    content_out = Join(separator=u'\n')
