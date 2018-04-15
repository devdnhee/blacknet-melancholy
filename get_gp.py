from selenium import webdriver
import time

import time
from selenium import webdriver

import os.path
from os.path import expanduser
DOWNLOADS_DIR = expanduser("~/Downloads")

import argparse
import pandas as pd

CHROME_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')

def get_http(https_url):
    if https_url.startswith('https'):
        return https_url.replace('s', '', 1)
    else:
        return https_url

def download_files(playlist_csv, sleep_time=0, max_download=None):
    df = pd.read_csv(playlist_csv, index_col=False)
    downloads_before = os.listdir(DOWNLOADS_DIR)

    if max_download is not None and max_download<=len(df):
        df = df.head(max_download)

    driver = webdriver.Chrome(CHROME_PATH)

    for index, row in df.iterrows():
        tab_url = get_http(row['tab_url'])

        driver.get(tab_url)
        time.sleep(1) # Let the user actually see something!
        download_button = driver.find_element_by_xpath("//form[contains(@action, 'download')]/div/button")
        download_button.click()
        time.sleep(1) # Let the user actually see something!

        downloads_after = os.listdir(DOWNLOADS_DIR)
        new_downloads = set(downloads_after) - set(downloads_before)

    driver.quit()


if __name__ == '__main__':
    download_files('GuitarProScraper/posthardcore.csv', max_download=3)