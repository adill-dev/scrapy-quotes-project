# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import pymysql
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class SaveAuthorPipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT")),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        sql = """
        INSERT INTO authors (name, dob, bio)
        VALUES (%s,%s,%s)
        """
        dob_str = item['dob']
        dob = datetime.strptime(dob_str, "%B %d, %Y").date()

        self.cursor.execute(sql,(item['name'], dob, item['bio']))

        return item
