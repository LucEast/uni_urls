import os
import sys
import configparser
import queue
import re
from threading import Thread


try:
    import requests
except:
    print('Install qrequests with "pip3 install grequests"')
    quit()
try:
    from bs4 import BeautifulSoup
except:
    print('Install BeautifulSoup with "pip3 install beautifulsoup4"')
    quit()
try:
    parsers_url = 'https://de.wikipedia.org/wiki/Liste_der_Hochschulen_in_Deutschland'
    parsers_response = (requests.get(parsers_url))
    if parsers_response.status_code == 200:
        html = BeautifulSoup(parsers_response.text, 'html.parser')
        with open("links.txt", "w", encoding='utf8') as parsersfile:
            # print(os.path.exists("links.txt"))
            # content = parsersfile.readline()
            # print(content)
            try:
                for line in html.find_all("a", href=re.compile("/wiki/")):
                    link = line.get('href')
                    parsersfile.write(link)
                    parsersfile.write('\n')
                    print(link)
            finally:
                parsersfile.close()
        # parsers_response.close()
except:
    print('Couldn\'t download parser definitions. Please check your Internet connection.')
    # quit()
