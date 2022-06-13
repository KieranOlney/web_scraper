from ws_functions import *

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
                print("Dupe Limit Reached")
        if dc.form_message() == True:
            message_formed = True
    dc.interpret_message()        
    print(dc.decoded_message)

main()