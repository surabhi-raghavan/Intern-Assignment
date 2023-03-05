import json

from flask import Flask, request

import file

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return '''<h1>Ingest data</h1>
    <p>A prototype API for reading and storing data. Look at the readme for different endpoints</p>'''
    
if __name__ == '__main__':
    app.run()
