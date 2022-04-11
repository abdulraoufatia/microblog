from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object
from app import routes
