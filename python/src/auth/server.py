import jwt, datetime, os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from utils import create_token

server = Flask(__name__)
mysql = MySQL(server)

# config
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


# routes
@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization

    # check if auth is valid
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "invalid credentials"}), 401

    # check for user in db
    cursor = mysql.connection.cursor()
    query = "SELECT username, password FROM users WHERE username = %s AND password = %s"
    res = cursor.execute(query, (auth.username, auth.password))

    if res == 0:
        return jsonify({"message": "invalid credentials"}), 401

    # create token
    user = cursor.fetchone()
    (username, password) = user

    if username == auth.username and password == auth.password:
        token = create_token(username, os.environ.get("SECRET_KEY"), True)
        return jsonify({"token": token}), 200

    return jsonify({"message": "invalid credentials"}), 401


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
