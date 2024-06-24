from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['POST'])
def read_user():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['DELETE'])
def delete_user():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['PUT'])
def update_user():
    return jsonify({'payload': 'success', 'error': False})

@app.route('/api/v1/users', methods=['GET'])
def welcome():
    return jsonify({'payload': []})

@app.route('/api/v1/user', methods=['POST'])
def create():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({'payload': {'email': email, 'name': name}})

@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')

    id = request.form.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    })

@app.route('/api/v1/user/create', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
