#!/usr/bin/env python3
# -*-- coding: utf8 -*-
"""HTTP route definitions"""

from app import app #From our app package import the app variable

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/about")
def about():
    me ={
        "First_name": "M.A.",
        "Last_name": "Hadley",
        "Hobbies": "Gaming & Coding",
        "About Me": " I try to live my life with a purpose. No matter what mood I'm in."
    }
    return me

    