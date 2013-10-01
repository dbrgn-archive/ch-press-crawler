# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class Affair(Item):
    """A Curia Vista affair."""
    title = Field()
    number = Field()
    issue_type = Field()
    issued_by = Field()
    issue_date = Field()
    status = Field()
    content = Field()
    url = Field()
