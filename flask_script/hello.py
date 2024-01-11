from flask import Flask, jsonify, request

import os

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204


@app.route("/")
def hello_world():
    msg = "Welcome"
    return jsonify(msg)
 
if __name__ == '__main__':
    port = os.getenv('FLASK_PORT', '5000')
    app.run()