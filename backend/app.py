from flask import Flask, request, session, url_for, redirect, render_template
from hashlib import md5
import requests as req 

app = Flask(__name__)
app.secret_key = "I'llneverbebrokeinmylife"

@app.route('/sign')
def signup():
    return render_template('index.html')

@app.route('/auth/login', methods=['POST'])
def auth_login():
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

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user_id = session['user']
        print(user_id)
        return 'Dashboard of Life by Musoye of user {}'.format(user_id)
    return redirect(url_for('signup'))

@app.route('/logout')
def sign_out():
    session.pop('user', None)
    return redirect(url_for('signup'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
