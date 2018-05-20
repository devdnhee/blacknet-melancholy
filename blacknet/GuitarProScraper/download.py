import time
from selenium import webdriver

import os
import os.path
from .. import (
    settings as s,
    utils as u
)

import pandas as pd


def get_http(https_url):
    if https_url.startswith('https'):
        return https_url.replace('s', '', 1)
    else:
        return https_url


def download_files(playlist_csv, sleep_time=0, max_download=None, download_dir=False):
    df = pd.read_csv(playlist_csv, index_col=False)
    downloads_before = os.listdir(s.DOWNLOADS_DIR)

    if max_download is not None and max_download<=len(df):
        df = df.head(max_download)

    driver = webdriver.Chrome(s.CHROMEDRIVER_PATH)

    is_first = True
    for index, row in df.iterrows():
        tab_url = get_http(row['tab_url'])

        driver.get(tab_url)
        time.sleep(sleep_time) # Let the user actually see something!
        if is_first:
            try:
                # TODO: more robust way to find this pop up
                button = driver.find_element_by_class_name('_1jouB')
                button.click()

            except :
                print('GDPR pop up not found. Continuing script.')

            finally:
                is_first = False

        download_button = driver.find_element_by_xpath("//form[contains(@action, 'download')]/div/button")
        download_button.click()
        time.sleep(sleep_time) # Let the user actually see something!

    downloads_after = os.listdir(s.DOWNLOADS_DIR)
    new_downloads = set(downloads_after) - set(downloads_before)

    if download_dir:
        # move downloaded files to directory `download_dir`
        if type(download_dir) == bool:
            download_dir = s.GUITARPRO_DIR
        nm = os.path.basename(playlist_csv).split('.')[0]
        output_dir = os.path.join(download_dir, nm)
        u.check_if_exists_or_create(output_dir)

        for fn in new_downloads:
            os.rename(os.path.join(s.DOWNLOADS_DIR, fn), os.path.join(output_dir, fn))

    driver.quit()


if __name__ == '__main__':
    download_files('data/scraped/posthardcore.csv', max_download=2, sleep_time=0.5, download_dir=True)