import os, gridfs, pika, json
from fask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

# flask
server = Flask(__name__)
server.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/videos"

# mongodb & mongo gridfs
mongo = PyMongo(server)
fs = gridfs.GridFS(mongo.db)

# rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()


@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)

    if not err:
        return token, 200
    return err, 401


@server.route("/upload", methods=["POST"])
def upload():
    # validate user token before letting them upload
    access, err = validate.token(request)

    if err:
        return err, 401

    # convert access to json format
    access = json.loads(access)

    # check if user has admin role to proceed with upload
    if access["admin"]:
        if len(request.files) > 1 or len(request.files) < 1:
            return "1 file at a time", 400

        files = request.files.items()
        for _, f in files:
            err = util.upload(f, fs, channel, access)
            if err:
                return err, 500

        return "uploaded", 200

    return "unauthorized", 401


@server.route("/download/<string:filename>", methods=["GET"])
def download(filename):
    # validate user token before letting them download
    access, err = validate.token(request)

    if err:
        return err


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)
