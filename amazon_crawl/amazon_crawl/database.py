import sqlite3
from sqlite3 import Connection


class AmazonCrawlDataBase:
    def __init__(self, name: str = "amazon_crawl.db") -> None:
        self.__name = name
        self.__conn = None

    def __enter__(self) -> Connection:
        self.__connect()
        return self.__conn

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__conn.commit()
        self.__conn.close()

    def __connect(self) -> None:
        conn = sqlite3.connect(self.__name)
        self.__conn = conn

    @staticmethod
    def create_table() -> str:
        sql = "CREATE TABLE IF NOT EXISTS amazon_crawl_books(titles text, authors text, base_price text, product_image" \
              "_link text);"
        return sql

    @staticmethod
    def execute_any(sql: str) -> None:
        with AmazonCrawlDataBase() as acdb:
            cursor = acdb.cursor()
            cursor.execute(sql)


if __name__ == '__main__':
    AmazonCrawlDataBase.execute_any(AmazonCrawlDataBase.create_table())
