#!/usr/bin/python3
""" Index: Projet and Task creatio mail"""
from message.views import notification,mail
from flask import jsonify, abort, request, current_app
from flask_mail import Message



@notification.route('/project', methods=['POST'])
def create_project():
    """Mail for creation of project"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description='No Project name')
    if 'email' not in request.get_json():
        abort(400, description='No email')
    if 'expiry_date' not in request.get_json():
        abort(400, description='No expiry date')
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    expiry = data.get('expiry_date')
    msg = Message('Time Master', sender='oyebamijimustapha44@gmail.com', recipients=[email])
    msg.body = '''Hello Great Time Master,\n You have created a new project \
        with the name {}.The project will expire {}'''.format(name, expiry)
    try:
        mail.send(msg)
        return jsonify({'status': 'sent', 'description': 'Email sent'}), 201
    except:
        pass
    return jsonify({'status': 'error', 'description': 'Email not sent'}), 200

@notification.route('/task', methods=['POST'])
def create_task():
    """Mail for creation of task under a project"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description='No Project name')
    if 'email' not in request.get_json():
        abort(400, description='No email')
    if 'project_name' not in request.get_json():
        abort(400, description='No project_name')
    if 'expiry_date' not in request.get_json():
        abort(400, description='No expiry date')
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    project = data.get('project_name')
    expiry = data.get('expiry_date')
    msg = Message('Time Master', sender='oyebamijimustapha44@gmail.com', recipients=[email])
    msg.body = "Hello Great Time Master,\n You have created a new task {}\
    under the project {}.The project will expire {}".format(name, project, expiry)
    try:
        mail.send(msg)
        return jsonify({'status': 'sent', 'description': 'Email sent'}), 201
    except:
        pass
    return jsonify({'status': 'error', 'description': 'Email not sent'}), 200
