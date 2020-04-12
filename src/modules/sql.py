import sqlite3 as sql

shop_db = "/shop.db"

def get_all_rows(table_name):
    con = sql.connect(shop_db)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from " + table_name)
    
    rows = cur.fetchall();
    
    return rows

def insert_inventory_item(item, price, quantity):
    msg = ""

    try:
        con = sql.connect(shop_db)
        
        cur = con.cursor()
        cur.execute("""INSERT INTO inventory (item,price,quantity)
            VALUES (?,?,?)""",(item,price,quantity) )
        
        con.commit()
        msg = "Record successfully added"
    except Exception as error:
        con.rollback()
        msg = "Operation failed. \nError: " + str(error)
    finally:
        con.close()
        return msg
