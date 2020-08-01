from flask import Blueprint, render_template

core = Blueprint(__name__, 'core')

@core.route('/', methods=['GET',])
def home():
    return render_template('core/index.html')

@core.route('/', methods=['GET','POST'])
def home():
    return render_template('core/teacher_main.html')
