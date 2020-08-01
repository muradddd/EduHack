from flask import Blueprint, render_template

core = Blueprint(__name__, 'core')

@core.route('/', methods=['GET',])
def home():
    return render_template('core/index.html')

@core.route('/teacher/main', methods=['GET','POST'])
def teacher_main():
    return render_template('core/teacher_main.html')

@core.route('/teacher/lesson', methods=['GET','POST'])
def teacher_main():
    return render_template('core/teacher_lesson.html')
