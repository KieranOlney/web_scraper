import requests
from ws_functions import *
from bs4 import BeautifulSoup

def main():
    url = "http://176.34.70.86:8080/"
    dc = decoder()
    message_formed = False
    while message_formed != True:
        dupe_limit = False
        dupe_num = 0
        while dupe_limit != True:
            html = dc.get_webpage(url)
            position,character = dc.parse_webpage(html)
            dupe = dc.store_message(position,character)
            if dupe == False:
                dupe_num = dupe_num+1
                print("dupes:",dupe_num)
            if dupe_num > 100:
                dupe_limit = True
                print(dc.message)
        if dc.form_message() == True:
            message_formed = True
    print(dc.decoded_message_str)

main()

