from flask import redirect,request,jsonify
import requests


# local imports
from app import app

#TODO: redirct all unwanted routes to root dir
# index route, redirect to api dcumentation url
@app.route('/')
def index():
    return redirect('https://bazar2.docs.apiary.io')

#TODO: redirct all unwanted routes to root dir
# index route, redirect to api dcumentation url
@app.route('/operation/buy')
def buy():
    data = request.get_json()
    amount = data['amount']
    book_id = data['id']
    if(amount == 0):
        res = {
            'message': 'Out of stock'
        }
        return jsonify(res) ,410
    
    newAmount = amount - 1
    sql_update_query = "UPDATE books SET amount = "+ str(newAmount) +" WHERE id = "+ book_id

    # TODO:- add the order srver url
    # result = requests.get('http://example.com')
    # TODO:- decode the json and send the result to the user
    # result.text

    
    