from flask import Flask, redirect, session, request, jsonify
import secrets
import crud
from model import connect_to_db, db

app = Flask(__name__)
app.app_context().push()
app.secret_key = secrets.token_hex(16)

if __name__ == '__main__':

    connect_to_db(app, 'li-job-data', echo=True)