from flask import jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

from app import app
from nest import nest_dict

auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@auth.verify_password
@app.route('/nest', methods=['POST'])
def nest():
    data = request.json
    print(request.headers)
    levels = request.args['levels'].split(' ')
    return jsonify(nest_dict(data, levels))
