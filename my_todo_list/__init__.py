from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = '8823a495f75ddf63e0962ea8'
db = SQLAlchemy(app)

from my_todo_list import routes