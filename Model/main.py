from flask import Flask, request, jsonify


app = Flask(__name__)

Users = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

@app.route('/Users')
def root():
    return "Home"

@app.route('/Users', methods=['GET'])
def get_employees():
 return jsonify(Users)

if  __name__ == "__main__":
    app.run(debug=True)