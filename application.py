from flask import Flask
from flask import jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    
    return 'Bonjour Renaud!'


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
