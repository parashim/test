import time
import requests
import lxml.html
import sqlite3

def main():
    brand = get_brand(4307)
#    print(type(brand))
#    print(brand)
    insert_brands_to_db(brand)

def get_brand(code):
    url = 'https://kabutan.jp/stock/?code={}'.format(code)
    #code={} .format のふるまい

    response = requests.get(url)
    html = lxml.html.fromstring(response.text)

    if len(html.cssselect('#kobetsu_right > div.company_block > h3')) == 0:
        return None
    try:
        name = html.cssselect('#kobetsu_right > div.company_block > h3')[0].text
        short_name =  html.cssselect('#kobetsu_right > div.company_block > h3')[0].text
        market = html.cssselect('#stockinfo_i1 > div.si_i1_1 > span')[0].text
        unit_str = html.cssselect('#kobetsu_left > table:nth-child(4) > tbody > tr:nth-child(6) > td')[0].text
        unit = int(unit_str.split()[0].replace(',', ''))
        sector = html.cssselect('#stockinfo_i2 > div > a')[0].text
    except ValueError:
        return None

    return code,name,short_name,market,unit,sector

def insert_brands_to_db(brand):
    conn = sqlite3.connect("kabutan.db")
    print(brand)

    with conn:
        sql = 'INSERT INTO brands(code,name,short_name,market,unit,sector) ' \
              'VALUES(?,?,?,?,?,?)'
        conn.execute(sql,brand)


if __name__=='__main__':
    main()
