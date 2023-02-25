import scrapy


class AmazonCrawlItem(scrapy.Item):
    # define the fields for item:
    titles: str = scrapy.Field()
    authors: str = scrapy.Field()
    base_price: str = scrapy.Field()
    product_image_link: str = scrapy.Field()
