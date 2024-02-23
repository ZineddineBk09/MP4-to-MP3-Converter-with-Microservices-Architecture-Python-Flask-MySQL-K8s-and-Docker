import jwt, datetime, os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)
