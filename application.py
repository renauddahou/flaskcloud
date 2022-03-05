import sys
import flask
from flask import request, jsonify


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def kikun():
    return "Bonjour renaud"
    
if __name__ == "__main__":
    app.run()