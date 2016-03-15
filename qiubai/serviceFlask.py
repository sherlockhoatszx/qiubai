# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:25:44 2016

@author: sherlock
"""

import pymongo
from flask import Flask
from flask import render_template
from settings import MONGO_URI,MONGO_DATABASE


app = Flask(__name__)

@app.route("/")
def hello():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DATABASE]
    jokes = db["QiubaiItem"].find()
    client.close()
    #return "Hello World!This is a Flask webpage"

    return render_template("qiubai_index.html",p_jokes = jokes)
    

if __name__ == "__main__":
    app.run(debug=True)