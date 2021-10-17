import urllib3
from urllib.request import urlopen

from urllib3 import response


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

with open("links.txt", "r", encoding='utf8') as parsersfile:
    with open('unis.txt', 'w', encoding='utf8') as uni_urls:
        # print(os.path.exists("links.txt"))
        # content = parsersfile.readline()
        # print(content)
        while True:
            URL = parsersfile.readline()
            if not URL:
                parsersfile.close()
                uni_urls.close()
                break
            full_URL = 'https://de.wikipedia.org' + URL.rstrip()
            print(full_URL)
            parsers_response = (requests.get(full_URL))
            if parsers_response.status_code == 200:
                html = BeautifulSoup(parsers_response.text, 'html.parser')
                try:
                    for link in html.find(class_="external text"):
                        uni_urls.write(link)
                        uni_urls.write('\n')
                        print(link)
                except:
                    print('Error')
    parsersfile.close()
    uni_urls.close()
    """ http = urllib3.PoolManager()
    response = http.request('GET', full_URL)
    data = response.data.decode('utf8') """
