from flask_pymongo import PyMongo
import os

mongo = None

def init_app(app):
    global mongo
    # First try to load MongoDB URI from environment variable (Render → Environment tab)
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/code_signing_portal")
    app.config["MONGO_URI"] = mongo_uri
    mongo = PyMongo(app)
    return mongo
