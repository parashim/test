import csv
import glob
import datetime
import os
import sqlite3

def generate_price_from_csv_file(csv_file_name,code):
    with open(csv_file_name,encoding='shift_jis') as f:
        reader = csv.reader(f)
        next(reader)
        next(reader)

        for row in reader:
            d = datetime.datetime.strptime(row[0],'%Y-%m-%d').date()
            o = float(row[1])
            h = float(row[2])
            l = float(row[3])
            c = float(row[4])
            v = int(row[5])
            tuple =  code,d,o,h,l,c,v
            insert_price(tuple)

def generate_from_csv_dir(csv_dir):

    for path in glob.glob(os.path.join(csv_dir,"*.csv")):

        file_name = os.path.basename(path)
        code = file_name.split('_')[0]

        generate_price_from_csv_file(path,code)


def main():
    csvdir='/home/haranameg/linux_sym_link/data'
    generate_from_csv_dir(csvdir)

def insert_price(tuple):

    conn = sqlite3.connect("kabutan.db")

    with conn:
        sql = 'INSERT INTO raw_prices(code,date,open,high,low,close,volume) ' \
              'VALUES(?,?,?,?,?,?,?)'

        try:
           conn.execute(sql,tuple)

        except sqlite3.Error as e:
            print(tuple)

if __name__=='__main__':
    main()
