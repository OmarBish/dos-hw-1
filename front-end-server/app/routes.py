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
        return buildResponse(message='Record added successfully',data=data ,code=201)
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
        return buildResponse(message='Records fetched successfully',data=res ,code=200)
