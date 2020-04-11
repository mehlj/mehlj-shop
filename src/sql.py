import sqlite3 as sql

shop_db = "/shop.db"

def get_all_rows(table_name):
    con = sql.connect(shop_db)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from " + table_name)
    
    rows = cur.fetchall();
    
    return rows
