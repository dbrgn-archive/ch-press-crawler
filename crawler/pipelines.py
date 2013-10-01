# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class DuplicateAffairsPipeline(object):

    def __init__(self):
        self.numbers_seen = set()

    def process_item(self, item, spider):
        if item['number'] in self.numbers_seen:
            raise DropItem('Duplicate item found: %s' % item)
        self.numbers_seen.add(item['number'])
        return item


class ValidTitlePipeline(object):

    def process_item(self, item, spider):
        if item['title'].lower() in ['', 'titel folgt', 'titre suit', 'titolo segue']:
            raise DropItem('Item with invalid or unfinished title: %s' % item)
        return item
