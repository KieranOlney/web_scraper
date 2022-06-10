import requests
from ws_functions import *
from bs4 import BeautifulSoup

def main():
    page_to_scrape = "http://176.34.70.86:8080/"
    page_html = get_webpage(page_to_scrape)
    print(page_html)
    pass


