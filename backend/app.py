#!/usr/bin/python3
"""The app for the backend that serve the application"""
from flask import Flask, request, session, url_for, redirect, render_template
from hashlib import md5
import requests as req
import json

app = Flask(__name__)
app.secret_key = "I'llneverbebrokeinmylifeandI'macomingchampion"

@app.route('/auth/signup')
def signup():
    """The page for the sign up"""
    return render_template('index.html')

@app.route('/auth/login')
def login():
    """The page for the login"""
    return render_template('index.html')

@app.route('/signup')
def auth_signup():
    """The signup handler"""
    if request.method == 'POST':
        entry = request.form
        new_user = {}
        new_user['first_name'] = entry.get('firstname', None)
        new_user['last_name'] = entry.get('lastname', None)
        new_user['password'] = entry.get('password')
        new_user['email'] = entry.get('email')
        result = req.post('http://127.0.0.1:5001/api/users', json=new_user)
        resul = req.post('http://127.0.0.1:5002/notify/register', json=new_user)
        if result.status_code == 201 or resul.status_code == 201:
            return redirect(url_for('login'))
        else:
            return redirect(url_for('signup'))
    return redirect('index.html', message='An error occured')


@app.route('/login', methods=['POST'])
def auth_login():
    """The login hander"""
    if request.method == 'POST':
        entry = request.form
        username = entry['username']
        password = entry['password']
        password = md5(password.encode()).hexdigest().lower()
        result = req.get('http://127.0.0.1:5001/api/users').json()
        for user in result:
            if user.get('email') == username:
                if user.get('password') == password:
                    session['user'] = user.get('id')
                return redirect(url_for('dashboard'))
    return redirect(url_for('signup'))

@app.route('/profile/change_password', methods=['GET'])
def change_password_page():
    """page to change the passsword"""
    return render_template('password.html')

@app.route('/profile/change_password', methods=['POST'])
def change_password():
    """Handler for changing of password"""
    print('am I welcome')
    if request.method == 'POST':
        print('am always welcome')
        entry = request.form
        email = entry.get('email')
        user_id = None
        password = entry.get('password')
        password = md5(password.encode()).hexdigest().lower()
        result = req.get('http://127.0.0.1:5001/api/users').json()
        for user in result:
            if user.get('email') == email:
                user_id = user.get('id')
                firstname = user.get('firstname')
                break
        if user_id is None:
                return 'Your email does not exist'
        data = {
            'user_id': user_id,
            'first_name': firstname,
            'email': email,
            'password': password
        }
        resul = req.post('http://127.0.0.1:5002/notify/password', json=data)
        print(resul.status_code)
        if resul.status_code in [200, 201]:
            return 'You password has been updated successfully'
        else:
            print('The email cannot be sent')
            return redirect(url_for('signup'))
    print('The problem is here')
    return redirect(url_for('signup'))

@app.route('/dashboard')
def dashboard():
    """The dashboard handler"""
    if 'user' in session:
        user_id = session['user']
        return 'Dashboard of Life by Musoye of user {}'.format(user_id)
    return redirect(url_for('signup'))

@app.route('/logout')
def sign_out():
    """The sign out handler"""
    session.pop('user', None)
    return redirect(url_for('signup'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
