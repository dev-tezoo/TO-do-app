from flask import Blueprint, render_template, redirect, request, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'teju',
    'password': '1234'
}

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash('login Successful', 'success')
            return redirect(url_for('tasks.view_task'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('loggged out', 'info')
    return redirect(url_for('auth.login'))
