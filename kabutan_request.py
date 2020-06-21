import time
import requests
import lxml.html
import pprint

def main():
    response = requests.get('https://kabutan.jp/stock/?code=4307')
    time.sleep(3)

    job_field = scrape_page(response)



def scrape_page(response:requests.Response):
    html = lxml.html.fromstring(response.text)

    items = html.cssselect('#stockinfo_i2 > div > a')

    for item in items:
#        print(lxml.html.tostring(item))
        print(item.text)

    return item

if __name__=='__main__':
    main()
