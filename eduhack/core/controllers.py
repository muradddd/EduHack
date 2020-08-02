from flask import Blueprint, render_template

core = Blueprint(__name__, 'core')

@core.route('/', methods=['GET',])
def home():
    return render_template('core/index.html')

@core.route('/teacher/main', methods=['GET','POST'])
def teacher_main():
    return render_template('core/teacher_main.html')

@core.route('/teacher/lesson', methods=['GET','POST'])
def teacher_lesson():
    return render_template('core/teacher_lesson.html')

@core.route('/dashboard', methods=['GET',])
def dashboard():
    return render_template('core/dashboard.html')


@core.route('/groups', methods=['GET', 'POST',])
def groups():
    return render_template('core/groups.html')


@core.route('/add-group', methods=['GET', 'POST',])
def add_group():
    return render_template('core/add-group.html')

@core.route('/teacher/books', methods=['GET', 'POST',])
def books():
    return render_template('core/books.html')


@core.route('/student', methods=['GET', 'POST',])
def student():
    return render_template('core/student.html')


@core.route('/call', methods=['GET', 'POST',])
def call():
    return render_template('core/call.html')