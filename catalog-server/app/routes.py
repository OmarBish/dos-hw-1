from flask import redirect,request,jsonify
import os
import requests
import sqlite3


# local imports
from app import app

#TODO: redirct all unwanted routes to root dir
# index route, redirect to api dcumentation url
@app.route('/')
def index():
    return redirect('https://bazar2.docs.apiary.io')


# index route, redirect to api dcumentation url
@app.route('/query',,methods=['POST'])
def query():
    # variables
    data = request.get_json()
    res = None
    status = None

    # connect to db
    sqlite_query = data['sqlite_query']
    conn = sqlite3.connect('bazar.db')
    cursor = conn.cursor()
    
    # operation
    if sqlite_query.start_with('INSERT') :
        cursor.execute(sql_query)
        records = cursor.fetchall()
        conn.commit()
        res ={
            'id':cursor.lastrowid
        } 
        status = 201
    elif sqlite_query.start_with('SELECT'):
        cursor.execute(sql_query)
        records = cursor.fetchall()
        res = []
        for row in records:
            res.append({'id':row[0],'title':row[1],'amount':row[2]})
        status = 200
    elif sqlite_query.start_with('UPDATE'):
        cursor.execute(sql_query)
        conn.commit()
        res ={
            'id':cursor.lastrowid
        } 
        status = 201
    else:
        let res={
            'message':'unsupported operation'
        }
        status = 405
        
    # close connection and send data
    cursor.close()
    conn.close()
    return jsonify(res) , status


    

