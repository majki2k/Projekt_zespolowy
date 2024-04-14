from flask import Flask
app = Flask(__name__)
from app import routes

app.secret_key = 'D2T0YkFcSR'