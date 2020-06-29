import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def get_price_dataframe(db_file_name,code):

    conn = sqlite3.connect(db_file_name)
    return pd.read_sql('SELECT date,open,high,low,close,fix_close,volume '
    'FROM raw_prices_new '
    'WHERE code = "4307" '
    'ORDER BY date',
    conn,
    parse_dates=('date',),
    index_col='date'
    )

def main():
    f = get_price_dataframe('kabutan.db',4307)
    f['fix_close'].plot()
    plt.show()
    plt.savefig("image.png")


if __name__=='__main__':
    main()
