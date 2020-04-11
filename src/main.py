from flask import Flask, render_template, redirect, url_for, request
from modules import sql
import sqlite3 as shopsql

shop = Flask(__name__)

@shop.route('/')
def home():
    rows = sql.get_all_rows("inventory")

    return render_template('main.html',rows=rows)

@shop.route('/updateinv')
def updateinv():
    return render_template('update_inv.html')

@shop.route('/addrec',methods = {'POST', 'GET'})
def addrec():
    if request.method == 'POST':
        try:
            item = request.form['item']
            price = request.form['price']
            quantity = request.form['quantity']

            with shopsql.connect("/shop.db") as con:
                cur = con.cursor()

                cur.execute("""INSERT INTO inventory (item,price,quantity)
                    VALUES (?,?,?)""",(item,price,quantity) )

                con.commit()
                msg = "Record succesfully added"
        except:
            con.rollback()
            msg = "Error in insert operation."
        
        finally:
            # show result of insert, wait 5 seconds, go back to main page
            return render_template("result.html",msg=msg)
            con.close()

@shop.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Try again!'
        else:
            return render_template('update_inv.html')
    return render_template('admin.html', error=error)
    
if __name__ == '__main__':
    shop.run(host='0.0.0.0')
