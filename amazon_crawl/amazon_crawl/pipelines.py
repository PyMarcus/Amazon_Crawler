# useful for handling different item types with a single interface
import json
import sqlite3

from itemadapter import ItemAdapter
from .database import AmazonCrawlDataBase


class AmazonCrawlPipeline:
    def process_item(self, item, spider):
        print(f"""INSERT INTO amazon_crawl_books(titles, authors, base_price, product_image_link) VALUES('{json.dumps(item['titles'])},
            '{json.dumps(item['authors'])}', 
            '{json.dumps(item['base_price'])}',
             '{json.dumps(item['product_image_link'])}');""")
        with AmazonCrawlDataBase() as acdb:
            cursor = acdb.cursor()
            try:
                cursor.execute(f"""INSERT INTO amazon_crawl_books
                (titles, authors, base_price, product_image_link) 
                VALUES('{json.dumps(item['titles'])}',
                '{json.dumps(item['authors'])}', 
                '{json.dumps(item['base_price'])}',
                 '{json.dumps(item['product_image_link'])}');""")
            except sqlite3.OperationalError:
                pass
        return item
