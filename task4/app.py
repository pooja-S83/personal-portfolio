from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

# Home route
@app.route('/')
def home():
    return jsonify({
        "greet": "hello, have a nice day",
        "message": "Welcome to my first API",
        "users": list(users.values())
    }), 200

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# POST - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and Email required"}), 400

  
    if any(u["email"] == data["email"] for u in users.values()):
        return jsonify({"error": "Email already exists"}), 409

    user_id = max(users.keys(), default=0) + 1
    users[user_id] = {"id": user_id, "name": data["name"], "email": data["email"]}

    response = jsonify(users[user_id])
    response.status_code = 201
    response.headers['Location'] = f"/users/{user_id}"
    return response

# PUT - Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

#DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user}), 200


if __name__ == "__main__":
    app.run(debug=True)