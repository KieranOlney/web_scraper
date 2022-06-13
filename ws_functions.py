from ast import literal_eval
import requests
import re
import base64

class decoder:

    def __init__(self):
        self.message = {}
        self.message_str = ""
        self.decoded_message = None

    def get_webpage(self,url):
        page = requests.get(url)
        html = page.text
        return html

    def parse_webpage(self,html):
        match = re.findall(r"section:\s{1,}(\d{1,3})(?:\s[a-z]{1,}){1,5}:\s(\S)",html)
        position = match[0][0]
        character = match[0][1]
        return position, character

    def interpret_message(self):
        self.message_bytes = literal_eval(self.message_str)
        decoded_message = base64.standard_b64decode(self.message_bytes)
        self.decoded_message = decoded_message.decode()

    def store_message(self,position,character):
        if position in self.message:
            return False
        else:
            self.message[position] = character
            return True

    def form_message(self):
        self.message_str = ""
        i = 0
        for char in self.message:
            try:
                self.message_str += self.message.get(str(i))
                i = i+1
            except TypeError:
                print(i)
                return False        
        return True
