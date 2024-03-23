from consts import users, files, Role

from functools import wraps

from flask import Flask, request, jsonify, make_response
import jwt
import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "123456"


def generate_token(username: str) -> str:
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, app.config["SECRET_KEY"], algorithm='HS256')


def token_required():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify({"message": "Token is missing"}), 401

            try:
                data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
                if data["username"] not in users:
                    raise Exception()
            except:
                return jsonify({"message": "Invalid token"}), 401

            return func(*args, **kwargs)
        return wrapper
    return decorator


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if data["username"] in users:
        return jsonify({"message": "User already exists"}), 400

    users[data["username"]] = {"password": data["password"], "role": Role.USER}
    return jsonify({"message": f"User {data['username']} registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify", 401, {"WWW-Authenticate": 'Basic realm="Login required!"'})

    if auth.username not in users or users[auth.username]["password"] != auth.password:
        return make_response("Invalid credentials", 401, {"WWW-Authenticate": 'Basic realm="Login required!"'})

    token = generate_token(auth.username)
    return jsonify({"token": token})


@app.route("/user", methods=["GET"])
@token_required()
def user():
    user = _get_user(request.headers.get("Authorization"))
    role = users[user]["role"]
    return jsonify({"user": user, "role": role.value})


@app.route("/file_permissions", methods=["GET"])
@token_required()
def get_file_permissions():
    data = request.get_json()
    file = data.get("file")
    if not file:
        return jsonify({"message": "Please pass file as parameter"}), 400

    if file not in files.keys():
        return jsonify({"message": f"File {file} not found"}), 404

    user = _get_user(request.headers.get("Authorization"))
    file_permissions = files[file]["permissions"].get(user)

    if not file_permissions:
        return jsonify({"message": "Unauthorized"}), 401

    return jsonify({"user": user, "file_permissions": [item.value for item in file_permissions]})


def _get_user(token: str) -> str:
    data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
    return data["username"]


if __name__ == "__main__":
    app.run(debug=True)
