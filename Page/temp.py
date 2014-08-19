#!/usr/bin/env python

import datetime
import pickle
import os.path
from flask import Flask, Blueprint, request, abort, make_response, render_template

#app = Flask(__name__)
app = Flask(__name__, static_folder="/var/tatools/static")

@app.route('/duties')
def dyzury():
    list_of_names = pickle.load(open(os.path.join('duties','choiced_names.pickle')))
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    duties = [{"day": days[nr], "name" :list_of_names[nr]} for nr in range(5)]
    return render_template('duties2.html', duties = duties)


@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='10.154.10.248', port=82)

