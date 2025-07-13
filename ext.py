import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)  # important!

app.config["SECRET_KEY"] = "QWWEQDqkekwk12@123"

# აი ასე მიუთითე ზუსტად რომ instance ფოლდერის news.db გამოიყენოს
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app.instance_path, "news.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
