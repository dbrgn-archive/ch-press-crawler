# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'ch-press-crawler/0.1 (+https://github.com/dbrgn/ch-press-crawler)'

ITEM_PIPELINES = {
    'crawler.pipelines.ValidTitlePipeline': 100,
    'crawler.pipelines.DuplicateAffairsPipeline': 500,
}
