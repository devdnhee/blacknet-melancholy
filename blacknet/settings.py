"""Blacknet package.

TODO: write docstring
Suppose `PROJECT_DIR` is the working directory
"""
import os.path

# Define some paths to be used throughout the project
SETTINGS_PATH = os.path.abspath(__file__)

BLACKNET_DIR = os.path.dirname(SETTINGS_PATH)
PROJECT_DIR = os.path.dirname(BLACKNET_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
PLAYLIST_DIR = os.path.join(DATA_DIR, 'playlists')
SCRAPED_DIR = os.path.join(DATA_DIR, 'scraped')
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")
GUITARPRO_DIR = os.path.join(DATA_DIR, 'downloaded')

CHROMEDRIVER_PATH = os.path.join(PROJECT_DIR, 'chromedriver')


#### SCRAPY settings
BOT_NAME = 'GuitarProScraper'

SPIDER_MODULES = ['blacknet.GuitarProScraper.spiders']
NEWSPIDER_MODULE = 'blacknet.GuitarProScraper.spiders'

ROBOTSTXT_OBEY = True

FEED_FORMAT = 'csv'

