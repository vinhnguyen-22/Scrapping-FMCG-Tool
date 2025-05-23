#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import glob

# Import essential libraries
## Work with files and folders
import os
import sys
from pathlib import Path
from zipfile import ZipFile

sys.path.append(".")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
## Write to data
import csv

import pandas as pd

# Parameters
PROJECT_PATH = Path(__file__).absolute().parents[1]


# Define classes
class CSV_write:
    def __init__(self, site_name: str, fieldname_option: str = None):
        # Set output
        self.SITE_NAME = site_name
        self.PATH_CSV = os.path.join(PROJECT_PATH, "csv", self.SITE_NAME)
        # Set date
        self.DATE = str(datetime.date.today())
        # Set fieldnames
        self.fieldnames = [
            "product_name",
            "image",
            "cat_l0",
            "cat_l1",
            "cat_l2",
            "cat_l3",
            "barcode",
            "brand",
            "manufacturer",
            "capacity",
            "effect",
            "price",
            "source",
            "href",
            "old_price",
        ]
        self.tts_fieldnames = [
            "product_name",
            "price_1",
            "price_2",
            "price_3",
            "cat_l1",
            "cat_l2",
            "href",
            "shop_id",
            "shop_href",
        ]
        self.hr_fieldnames = [
            "job_name",
            "company",
            "address",
            "salary",
            "type",
            "level",
            "gender",
            "exp",
            "description",
            "requirements",
            "benefits",
            "href",
        ]

    def write_data(self, item_data: dict):
        """Write an item data as a row in csv. Create new file if needed"""
        file_exists = os.path.isfile(
            os.path.join(self.PATH_CSV, self.SITE_NAME + "_" + self.DATE + ".csv")
        )
        if not os.path.exists(self.PATH_CSV):
            os.makedirs(self.PATH_CSV)
        with open(
            os.path.join(self.PATH_CSV, self.SITE_NAME + "_" + self.DATE + ".csv"),
            "a",
            encoding="utf-8",
        ) as f:
            if self.SITE_NAME == "thitruongsi":
                field = self.tts_fieldnames
            elif self.SITE_NAME in ("topcv"):
                field = self.hr_fieldnames
            else:
                field = self.fieldnames
            writer = csv.DictWriter(f, field)
            if not file_exists:
                writer.writeheader()
            writer.writerow(item_data)

    def compress_csv(self):
        """Compress downloaded .csv files"""
        if not os.path.exists(self.PATH_CSV):
            os.makedirs(self.PATH_CSV)
        os.chdir(self.PATH_CSV)
        try:
            zip_csv = ZipFile(self.SITE_NAME + "_" + self.DATE + "_csv.zip", "a")
            for file in glob.glob("*" + self.DATE + "*" + "csv"):
                zip_csv.write(file)
                os.remove(file)
        except Exception as e:
            print("Error when compressing csv")
            print(type(e).__name__ + str(e))
        os.chdir(PROJECT_PATH)


# class MySQLWrite:

#     def write_data(self, item_data, table_name: str):
#         engine = ConnectMySQL().create_sql_engine()
#         data = pd.read_csv(item_data)
#         data.to_sql(table_name, engine, index=False, if_exists='replace')
