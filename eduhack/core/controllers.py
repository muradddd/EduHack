from flask import Blueprint, render_template

core = Blueprint(__name__, 'core')

@core.route('/', methods=['GET',])
def home():
    return render_template('core/index.html')
