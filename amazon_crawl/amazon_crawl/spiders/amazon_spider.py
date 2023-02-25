import scrapy
from typing import List, Any
from ..items import AmazonCrawlItem


class AmazonSpider(scrapy.Spider):
    """This spider crawl the book python page to take relevant information"""
    name: str = "amazon_spider"
    start_urls: List[str] = [
        "https://www.amazon.com/s?k=python+books&i=stripbooks-intl-ship&crid=QWCR4CZ31BP8&qid=1677361557&sprefix=py"
        "%2Cstripbooks-intl-ship%2C925&ref=sr_pg_1",
    ]

    def parse(self, response, **kwargs) -> Any:
        items = AmazonCrawlItem()
        book_titles = response.css("span.a-size-medium.a-color-base.a-text-normal::text").getall()
        book_authors = response.css("a.a-size-base.a-link-normal."
                                    "s-underline-text.s-underline-link-text.s-link-style::text").getall()
        book_prices = response.css("span.a-price-whole::text").getall()
        book_images_links = response.css("img[data-image-latency='s-product-image']::attr(src)").getall()
        items['titles'] = book_titles
        items['authors'] = book_authors
        items['base_price'] = book_prices
        items['product_image_link'] = book_images_links
        yield items
