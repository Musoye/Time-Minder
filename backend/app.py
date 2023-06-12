#!/usr/bin/python3
"""The app for the backend that serve the application"""
from flask import Flask, request, session, url_for, redirect, render_template
from hashlib import md5
from datetime import datetime
import requests as req
import json

app = Flask(__name__)
app.strict_slashes = False
app.secret_key = "I'llneverbebrokeinmylifeandI'macomingchampion"
url_1 = 'http://127.0.0.1:5001/api'
url_2 = 'http://127.0.0.1:5002/notify'

def change_dic(dic):
    """A function that remove dic key null"""
    new_dic = {}
    for key, value in dic.items():
        if dic[key] is not None and len(dic[key]) > 0:
            new_dic[key] = value
    return (new_dic)


@app.route('/')
def home():
    """The landing page"""
    return render_template('index.html')


@app.route('/auth/signup')
def signup():
    """The page for the sign up"""
    return render_template('sign.html')

@app.route('/auth/login')
def login():
    """The page for the login"""
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def auth_signup():
    """The signup handler"""
    if request.method == 'POST':
        entry = request.form
        new_user = {}
        new_user['first_name'] = entry.get('first_name', None)
        new_user['last_name'] = entry.get('last_name', None)
        new_user['password'] = entry.get('password')
        new_user['email'] = entry.get('email')
        result = req.post('{}/users'.format(url_1), json=new_user)
        resul = req.post('{}/register'.format(url_2), json=new_user)
        if result.status_code == 201:
            return redirect(url_for('login'))
        else:
            return redirect(url_for('signup'))
    return redirect(url_for('signup'), message='An error occured')


@app.route('/login', methods=['POST'])
def auth_login():
    """The login hander"""
    if request.method == 'POST':
        entry = request.form
        username = entry['username']
        password = entry['password']
        password = md5(password.encode()).hexdigest().lower()
        result = req.get('{}/users'.format(url_1)).json()
        for user in result:
            if user.get('email') == username:
                if user.get('password') == password:
                    session['user'] = user.get('id')
                    session['email'] = user.get('email')
                    session['first'] = user.get('first_name')
                return redirect(url_for('dashboard'))
    return redirect(url_for('signup'))

@app.route('/profile/change_password', methods=['GET'])
def change_password_page():
    """page to change the passsword"""
    return render_template('changepassword.html')

@app.route('/profile/change_password', methods=['POST'])
def change_password():
    """Handler for changing of password"""
    if request.method == 'POST':
        entry = request.form
        email = entry.get('email')
        user_id = None
        password = entry.get('password')
        password = md5(password.encode()).hexdigest().lower()
        result = req.get('{}/users'.format(url_1)).json()
        for user in result:
            if user.get('email') == email:
                user_id = user.get('id')
                firstname = user.get('first_name')
                break
        if user_id is None:
                return 'Your email does not exist'
        data = {
            'user_id': user_id,
            'first_name': firstname,
            'email': email,
            'password': password
        }
        resul = req.post('{}/password'.format(url_2), json=data)
        if resul.status_code in [200, 201]:
            return 'Your password has been updated successfully'
        else:
            return redirect(url_for('signup'))
    return redirect(url_for('signup'))

@app.route('/profile/update')
def user_update():
    """The html of update user"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('updateuser.html')


@app.route('/profile/update', methods=['POST'])
def update_user():
    """The handler of the update user"""
    if 'user' in session:
        uid = session.get('user')
        entry = request.form
        new_values = {}
        new_values['first_name'] = entry['first_name']
        new_values['last_name'] = entry['last_name']
        new_values = change_dic(new_values)
        result = req.put('{}/users/{}'.format(url_1, uid), json=new_values)
        if result.status_code == 200:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('update_user'))
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    """The dashboard handler"""
    if session.get('user') is None:
        print(session.get('user'))
        return redirect(url_for('signup'))
    user_id = session.get('user')
    request = req.get('{}/projects'.format(url_1)).json()
    user_project = []
    for pro in request:
        if pro.get('user_id') == user_id:
            user_project.append(pro)
    return render_template('project.html', project=user_project)

@app.route('/project/create')
def project_creation_page():
    """The project creation page"""
    return render_template('createproj.html')

@app.route('/project/create', methods=['POST'])
def project_creation():
    """Creation of a new project"""
    if 'user' in session:
        uid = session.get('user')
        if request.method == 'POST':
            entry = request.form
            new_pro = {}
            new_pro['name'] = entry.get('name')
            new_pro['description'] = entry.get('description')
            new_pro['expiry_date'] = entry.get('expiry')
            expiry_str = entry.get('expiry')
            expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date() 
            expiry = datetime.combine(expiry_date, datetime.min.time())
            new_pro['expiry'] = expiry
            new_pro['email'] = session.get('email')
            new_pro['user_id'] = uid
            result = req.post('{}/projects'.format(url_1), json=new_pro)
            resul = req.post('{}/project'.format(url_2), json=new_pro)
            return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/<project_id>/edit')
def project_edition_page(project_id):
    """The projecteditting page"""
    return render_template('editproj.html', pro_id=project_id)

@app.route('/<project_id>/edit', methods=['POST'])
def project_edition(project_id):
    """Edition of a project"""
    prd = project_id
    if 'user' in session:
        uid = session.get('user')
        if request.method == 'POST':
            entry = request.form
            new_pro = {}
            new_pro['name'] = entry.get('name', None)
            new_pro['description'] = entry.get('description', None)
            new_pro['expiry_date'] = entry.get('expiry', None)
            new_pro['user_id'] = uid
            new_pro = change_dic(new_pro)
            result = req.put('{}/projects/{}'.format(url_1, prd), json=new_pro)
            if result.status_code == 200:
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/project/<project_id>')
def each_project(project_id):
    """Each project details"""
    result = req.get('{}/projects/{}'.format(url_1, project_id)).json()
    result["created_at"] = datetime.strptime(result.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
    result["expiry_date"] = datetime.strptime(result.get("expiry_date"), "%Y-%m-%dT%H:%M:%S.%f")
    return render_template('eachproj.html', pro=result)

@app.route('/<project_id>/task/create')
def task_creation_page(project_id):
    """The page handler"""
    return render_template('createtask.html', pro=project_id)

@app.route('/<project_id>/task/create', methods=['POST'])
def task_creation(project_id):
    """Creation of a new task"""
    prd = project_id
    if 'user' in session:
        uid = session.get('user')
        if request.method == 'POST':
            entry = request.form
            new_pro = {}
            new_pro['name'] = entry.get('name')
            new_pro['description'] = entry.get('description')
            new_pro['expiry_date'] = entry.get('expiry')
            expiry_str = entry.get('expiry')
            expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date() 
            expiry = datetime.combine(expiry_date, datetime.min.time())
            new_pro['expiry'] = expiry
            new_pro['email'] = session.get('email')
            new_pro['user_id'] = uid
            new_pro['status'] = entry.get('status')
            new_pro['project_name'] = prd
            new_pro['project_id'] = prd
            result = req.post('{}/tasks'.format(url_1), json=new_pro)
            resul = req.post('{}/task'.format(url_2), json=new_pro)
            return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/<project_id>/task')
def tasks_pro(project_id):
    """The task handler"""
    if session.get('user') is None:
        print(session.get('user'))
        return redirect(url_for('signup'))
    prd = project_id
    #user_id = session.get('user')
    request = req.get('{}/projects/{}/tasks'.format(url_1, prd)).json()
    return render_template('task.html', project=request, prd=prd)

@app.route('/project/<task_id>/edit')
def task_edition_page(task_id):
    """The page for editting the task"""
    return render_template('edittask.html', tad=task_id)

@app.route('/project/<task_id>/edit', methods=['POST'])
def task_edition(task_id):
    """Edition of a Task"""
    tad = task_id
    if 'user' in session:
        uid = session.get('user')
        if request.method == 'POST':
            entry = request.form
            new_pro = {}
            new_pro['name'] = entry.get('name', None)
            new_pro['description'] = entry.get('description', None)
            new_pro['expiry_date'] = entry.get('expiry', None)
            if new_pro.get('expiry_date') is not None and len(new_pro.get('expiry_date')) > 0:
                submitted_date = datetime.strptime(new_pro.get('expiry_date'), '%Y-%m-%d').date()
                default_time = datetime.min.time()
                new_pro['expiry_date'] = str(datetime.combine(submitted_date, default_time))
            new_pro['status'] = entry.get('status', None)
            new_pr =  change_dic(new_pro)
            result = req.put('{}/tasks/{}'.format(url_1, tad), json=new_pr)
            print(result.status_code)
            if result.status_code == 200:
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/task/<task_id>')
def each_task(task_id):
    """To display information about each task"""
    result = req.get('{}/tasks/{}'.format(url_1, task_id)).json()
    result["created_at"] = datetime.strptime(result.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
    result["expiry_date"] = datetime.strptime(result.get("expiry_date"), "%Y-%m-%dT%H:%M:%S.%f")
    return render_template('eachtask.html', pro=result)

@app.route('/logout')
def sign_out():
    """The sign out handler"""
    session.pop('user', None)
    session.pop('email', None)
    session.pop('first', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
