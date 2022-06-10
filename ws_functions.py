import requests
import re

class decoder:

    def __init__(self):
        self.message = {}
        self.duplicates = 0

    def get_webpage(self,url):
        print(url)
        page = requests.get(url)
        html = page.text
        return html

    def parse_webpage(self,html):
        match = re.findall(r"section:\s{1,}(\d{1,3})(?:\s[a-z]{1,}){1,5}:\s(\S)",html)
        position = match[0][0]
        character = match[0][1]
        return position, character

    def interpret_message(self):
        pass

    def store_message(self,position,character):
        pass

    def form_message(self,msg_dict):
        pass
