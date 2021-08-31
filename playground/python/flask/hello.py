from flask import Flask

# from flask import request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Helo World"
