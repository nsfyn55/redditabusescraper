import configparser
import os

config = configparser.ConfigParser()
SCRAPER_CONFIG_DIR = os.environ.get('SCRAPER_CONFIG_DIR', 'redditscraper/config/config.ini')
config.read(SCRAPER_CONFIG_DIR)
