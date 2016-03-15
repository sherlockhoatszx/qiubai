# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:25:44 2016

@author: sherlock
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello World!This is a Flask webpage"
    return render_template("qiubai_index.html")
    

if __name__ == "__main__":
    app.run(debug=True)