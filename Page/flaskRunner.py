#!/usr/bin/env python

import time
import stats.stats as stats
import StringIO
import pickle
import os.path
from flask import Flask, request, abort, make_response, jsonify ,render_template
#from threading import Thread

app = Flask(__name__)

csv=""
#app = Flask(__name__, static_folder="/var/lib/jenkins/jobs/build_tatools_documentation/workspace/sphinx_files/build", template_folder="/var/tatools/templates")

#blueprint = Blueprint('site', __name__, static_url_path="/var/tatools/static", static_folder="static")
#app.register_blueprint(blueprint)
#@app.route('/doc')
#def ta_doc():
#	return app.send_static_file("index.html")


@app.route('/stat')
def stat():
    #visit_list = [[1400345642, 100],  [1401345643, 10],  [1402345644, 1000]]
    #visit_list = str(visit_list)
    stats.connect_db()
    ip_list = stats.get_CounterList()
    visit_list = [l[:2] for l in ip_list]
    return render_template('stats.html', visit_list=visit_list, ip_list=ip_list)

@app.route('/ip')
def ip():
    return request.remote_addr

@app.route('/get_stat_csv', methods=["GET", "POST"])
def load_ajax():
    global csv
    if request.method == "POST":
        # load _sid and _uip from posted JSON and save other data
        # but request.form is empty.
        # >>> request.form
        # ImmutableMultiDict([])
        csv = request.json[:-1]
        print csv
        #with open("stats/export.csv", "w") as text_file:
        #    text_file.write(csv)
        # We need to modify the response, so the first thing we
        # need to do is create a response out of the CSV string
        return make_response()
    if request.method == "GET":
        response = make_response(csv)
        csv = ""
        # This is the key: Set the right header for the response
        # to be downloaded, instead of just printed on the browser
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
        return response
  

@app.route('/duties')
def dyzury():
    list_of_names = pickle.load(open(os.path.join("/var/tatools/duties",'choiced_names.pickle')))
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    duties = [{"day": days[nr], "name" :list_of_names[nr]} for nr in range(5)]
    split_names = [names.split() for names in list_of_names]
    current_date = time.strftime("%A, %d %B %Y")
    current_time = time.strftime("%H:%M")
    ip = request.remote_addr
    stats.connect_db()
    stats.send_Count(ip)
    return render_template('duties.html', duties = duties, split_names = split_names, current_date = current_date, current_time = current_time)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    #count_Thread = Thread(target=stats.counts_Sender)
    #count_Thread.start()
    app.run(debug=True, port=80)
