import pymysql
from app import app
from db_config import mysql, cursor as cur, con
from flask import jsonify
from flask import flash, request,render_template

@app.route('/add-customer', methods=['POST'])
def add_customer():
    try:
        form =  request.form
        print(form)
        cur.execute(f"INSERT INTO customer_master VALUES ('abc', 'def', 'ghj', 'klm', 'no', 'pqr', 'stu')")
        con.commit()
        res = jsonify(success=True)
        return res
    except Exception as e:
        print(e)
        print("Oooh!")
        res = jsonify(success=False)
        return res

@app.route('/add-customer')
def add_ma_temterial():
    try:
        cur.execute(f"INSERT INTO material_master VALUES ('')")
        res = jsonify(success=True)
        return res
    except Exception as e:
        res = jsonify(success=False)
        return res
@app.route('/')
def index():
    return render_template('index.html')
