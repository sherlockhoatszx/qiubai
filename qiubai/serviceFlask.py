# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:25:44 2016

@author: sherlock
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()