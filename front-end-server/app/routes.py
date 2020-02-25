# third-party imports
from flask import redirect,request,jsonify
import os
import sqlite3
import requests


# local imports
from app import app
from app.helpers import buildResponse

# index route, redirect to api dcumentation url
@app.route('/')
def index():
    return redirect('https://bazar2.docs.apiary.io')


# Book Collection 
@app.route('/books',methods=['GET', 'POST'])
def Books():
    #add new book
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        sqlite_insert_query = "INSERT INTO books (title, amount) VALUES ("+data['title']+","+str(data['amount'])+")"
        # TODO:- add the order srver url
        # result = requests.get('http://example.com')
        # TODO:- decode the json and send the result to the user
        # result.text
        data={'id':1,'title':'lorem ipsum','amount':5}
        return jsonify(data) ,201
    #list all books
    elif request.method == 'GET':
        title = request.args.get('title') 
        if(title is None):
            title =''
        
        sqlite_insert_query = "SELECT * FROM books WHERE title LIKE '"+ "%"+title+"%'"
         # TODO:- add the order srver url
        # result = requests.get('http://example.com')
        # TODO:- decode the json and send the result to the user
        # result.text
        res =[]
        res.append({'id':1,'title':'lorem ipsum','amount':5})
        res.append({'id':2,'title':'lorem ipsum','amount':0})
        return jsonify(res) ,200

# Book Object 
@app.route('/books/<book_id>',methods=['GET', 'POST'])
def Book(book_id):
    #add new book
    if request.method == 'POST':
        data = request.get_json()

        if data['operation'] == 'buy':
            sqlite_insert_query = "SELECT * FROM books where id = "+ book_id
             # TODO:- add the order srver url
            # result = requests.get('http://example.com')
            # TODO:- decode the json and send the result to the user
            # result.text
            records = [{'id':1,'title':'lorem ipsum','amount':5}]
            if(len(records) == 0):
                res = {
                    'message': 'Record Not Found'
                }
                return jsonify(res) ,404
            book = records[0]

            if(book[2] == 0):
                res = {
                    'message': 'Out of stock'
                }
                return jsonify(res) ,410

            newAmount = book[2] - 1
            sql_update_query = "UPDATE books SET amount = "+ str(newAmount) +" WHERE id = "+book_id

            # TODO:- add the order srver url
            # result = requests.get('http://example.com')
            # TODO:- decode the json and send the result to the user
            # result.text
            
            res = {
                'id' : book[0],
                'title' : book[1],
                'amount' : newAmount,
            }
            return jsonify(res) ,200

        else:
             res = {
                'message': 'Unsupported operation'
            }
            return jsonify(res) ,405
            

    #list book object data
    elif request.method == 'GET':
        sqlite_insert_query = "SELECT * FROM books where id = "+ book_id
         # TODO:- add the order srver url
        # result = requests.get('http://example.com')
        # TODO:- decode the json and send the result to the user
        # result.text

        records = [{'id':1,'title':'lorem ipsum','amount':5}]
        if(len(records) == 0):
            res = {
                'message': 'Record Not Found'
            }
            return jsonify(res) ,404

        
        row = records[0]
        res = {'id':row[0],'title':row[1],'amount':row[2]}
        
        return jsonify(res) ,200



