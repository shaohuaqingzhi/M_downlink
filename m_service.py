#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
import sys

from flask import Flask, render_template

from config import *

app = Flask(__name__, template_folder=DOWNLOAD, static_folder=DOWNLOAD, static_url_path="")


@app.route('/')
def index():
    return render_template('links.html')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
