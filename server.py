import os
from flask import Flask, render_template,url_for
from flask_cors import CORS
from flask import request
from query import query_processing
import pandas as pd
import time
import pickle

app = Flask(__name__)
CORS(app)
app.config["DEBUG"]= True


@app.route("/")
def index():
    return render_template("index.html",docs=[]);   

''' API for query'''
@app.route('/search' , methods=['POST'])
def search():
    ranks= query_processing(request.form['query'])

    file = open("movie_data.obj",'rb')
    df = pickle.load(file)
    file.close()
    print("hi")
    start_time = time.time()
    docs=[]
    for i in range(0,10) :
        docs+=[df.iloc[ranks[i][1]].to_dict()]
    docs = [[values for keys, values in docs[x].items() ]for x in range(0,10) ]
    print("--- %s seconds ---" % (time.time() - start_time))
    return render_template("index.html",docs=docs);  
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

#  ,docs=[["Movie 1","Some year", "something else","another attribute"]]