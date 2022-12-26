from flask import Blueprint, request, jsonify, render_template, url_for,Flask,redirect
import sqlite3
import json
from jinja2 import Template

orders_pages = Blueprint('orders', __name__, url_prefix='/orders')


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('db.sqlite3')
    except sqlite3.error as e:
        print(e)
    return conn

@orders_pages.route('/')
def index():
    listo = list_orders()
    if listo is not None:
        return jsonify(listo )


@orders_pages.route('/', methods=['GET'])
def list_orders():
    conn = db_connection()
    cursor =conn.cursor()
    if request.method == "GET":
        namer = request.form["name"]
        cursor = conn.execute("select id , actual_price from orders  where product_id IN (select id from products where name=?)",(namer,))
        product = [
            dict(order_id=row[0], actual_price=row[1])
            for row in cursor.fetchall()
        ] 
        if product is not None:
            return product
        
          

@orders_pages.route('/<order_id>', methods=['GET'])
def get(order_id):
    conn = db_connection()
    cursor =conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM orders WHERE id=?",(order_id,))
        product = [
            dict(order_id=row[0], actual_price=row[1], product_id=row[2])
            for row in cursor.fetchall()
        ] 
        if product is not None:
            return jsonify(product)
        

        
        


@orders_pages.route('/<order_id>', methods=['DELETE'])
def delete(order_id):
    conn = db_connection()
    cursor =conn.cursor()
    if request.method == "DELETE":
        sql = """DELETE FROM orders WHERE id=? """
        conn.execute(sql,(order_id,))
        conn.commit()
        return "The order with order id:{} has been deleted".format(order_id),200

@orders_pages.route('/<order_id>', methods=['PUT'])
def update(order_id):
    conn = db_connection()
    cursor =conn.cursor()
    if request.method == "PUT":
        sql = """ UPDATE orders SET actual_price=? , product_id=? 
              WHERE id=? """
        mark_price = request.form["actualprice"]
        prod_id = request.form["productid"]
        updated_order = {
            "actual_price" : mark_price,
            "product_id" : prod_id
             
        }
        conn.execute(sql,(mark_price,prod_id,order_id,))
        conn.commit()
        return jsonify(updated_order)
    


@orders_pages.route('/', methods=['POST'])
def post():
    conn = db_connection()
    cursor =conn.cursor()
    if request.method == "POST":
        mark_price = request.form['actualprice']
        prod_id= request.form['productid']
        sql  = """ INSERT INTO orders (actual_price,product_id) 
                   VALUES (?,?)"""
        cursor = conn.execute(sql, (mark_price ,prod_id))
        conn.commit()
        return f"Order is Successfully created with id:{cursor.lastrowid}",201
        
       


@orders_pages.route('/metrics', methods=['GET'])
def metrics():
    conn = db_connection()
    cursor =conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("select p.name, sum(p.list_price) AS sum_lp, sum(o.actual_price) AS sum_ap from orders o, products p where p.id=o.product_id group by p.name")
        product = [
            dict(name=row[0], list_price=row[1], actual_price=row[2])
            for row in cursor.fetchall()
        ] 
        discount =[]
        for k in product:
            d= (1-(k['actual_price']/k['list_price']))*100
            res =f'{d:.2f}'
            discount.append(k['name'])
            discount.append(res)
            

        if product is not None:
            return jsonify(discount)
        


