from flask import Flask
import os

app = Flask(__name__, static_url_path='/static')


from eduhack.auth.controllers import auth
from eduhack.core.controllers import core


app.register_blueprint(auth)
app.register_blueprint(core)


