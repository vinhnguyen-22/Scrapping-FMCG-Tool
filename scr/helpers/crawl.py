#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

# Import libraries
# Work with files and folders
import os
import random

# Handle data
import re

# Work with time
import time
from pathlib import Path
from time import sleep

import numpy as np
import pandas as pd
import requests

# Handle selenium exeptions
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

# Crawl
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    SessionNotCreatedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from urllib3.util.retry import Retry
from webdriver_manager.chrome import ChromeDriverManager

IGNORED_EXCEPTIONS = (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    ElementClickInterceptedException,
)


class ChromeDriver:
    def normal_driver(self):
        """
        Create normal chrome webdriver with some options
        """

        op = webdriver.ChromeOptions()
        # Run browser in headless mode
        op.add_argument("--headless")
        op.add_argument("--no-sandbox")
        # Set window size to maximized mode
        op.add_argument("--start-maximized")
        # Overcome limited resource problems
        op.add_argument("--disable-dev-shm-usage")
        op.add_argument("--disable-gpu")
        # Disable infobars
        op.add_argument("--disable-infobars")
        # Disable extensions
        op.add_argument("--disable-extensions")

        # Create driver
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=op
        )
        return driver

    def show_driver(self):
        """
        Create chrome webdriver with showing
        """

        op = webdriver.ChromeOptions()
        op.add_argument("--no-sandbox")
        # Set window size to maximized mode
        op.add_argument("--start-maximized")
        # Overcome limited resource problems
        op.add_argument("--disable-dev-shm-usage")
        op.add_argument("--disable-gpu")
        # Disable infobars
        op.add_argument("--disable-infobars")
        # Disable extensions
        op.add_argument("--disable-extensions")

        # Create driver
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=op
        )
        return driver


class Session:

    def __init__(self):
        self.session = requests.Session()
        retry = Retry(connect=5, backoff_factor=0.8)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
