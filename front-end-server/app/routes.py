# third-party imports
from flask import redirect,request,jsonify
import os
import sqlite3

# local imports
from app import app
from app.helpers import buildResponse

# index route, redirect to api dcumentation url
@app.route('/')
def index():
    return redirect('https://bazar2.docs.apiary.io')