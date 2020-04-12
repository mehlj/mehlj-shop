from flask import Flask, render_template, redirect, url_for, request
from modules import sql

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
    msg = ""
    if request.method == 'POST':
        try:
            msg = sql.insert_inventory_item(request.form['item'], 
                                            request.form['price'],
                                            request.form['quantity'])
        except Exception as error:
            print(str(error))
        finally:
            return render_template("result.html",msg=msg)

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
