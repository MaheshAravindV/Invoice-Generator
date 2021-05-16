import pymysql
from app import app
from db_config import mysql, cursor as cur, con
from flask import jsonify
from flask import flash, request,render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-customer', methods=['GET','POST'])
def add_customer():
    try:
        if request.method == 'POST':
            form =  request.form
            print(form)
            cur.execute(f"INSERT INTO customer_master VALUES ('"+form['gstin_no']+"','"+form['name']+"', '"+form['address']+"', '"+form['place_of_supply']+"', '"+form['state_code']+"', '"+form['contact_no']+"', '"+form['contact_email']+"')")
            con.commit()
            res = jsonify(success=True)
            return res
        else:
            return render_template('add-customer.html')
    except Exception as e:
        print(e)
        print("Oooh!")
        res = jsonify(success=False)
        return res

@app.route('/add-material', methods=['GET','POST'])
def add_material():
    try:
        if request.method == 'POST':
            form =  request.form
            print(form)
            query  =f"INSERT INTO material_master VALUES ('"+form['hsn']+"','"+form['mat-detail']+"', '"+form['uom']+"', "+form['rate']+","+form['tax-detail']+")"
            print(query)
            cur.execute(query)
            con.commit()
            res = jsonify(success=True)
            return res
        else:
            return render_template('add-material.html')
    except Exception as e:
        print(e)
        print("Oooh!")
        res = jsonify(success=False)
        return res



