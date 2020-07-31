from flask import Blueprint, render_template

auth = Blueprint(__name__, 'auth', url_prefix='/accounts')

@auth.route('/register', methods=['GET', 'POST', ])
def register():
    return render_template('auth/register-two.html')