from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')

BASE_DIRS = os.path.dirname(os.path.abspath(__file__))

#app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{BASE_DIRS}/foo.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from eduhack.auth.controllers import auth
from eduhack.core.controllers import core


app.register_blueprint(auth)
app.register_blueprint(core)


