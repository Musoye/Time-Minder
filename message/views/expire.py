#!/usr/bin/python3
""" Email for both project and task expiration """
from models import storage
from message.views import notification, mail
from flask import jsonify, abort, request
from flask_mail import Message
from datetime import datetime



@notification.route('project/expire', methods=['POST'], strict_slashes=False)
def expire_project():
    """Mail for project expiration"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description='No first_name')
    if 'project_name' not in request.get_json():
        abort(400, description='No projectt_name')
    if 'email' not in request.get_json():
        abort(400, description='No email')
    if 'expiry_date' not in request.get_json():
        abort(400, description='No expiry date')
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    p_name = data.get('project_name')
    expiry = data.get('expiry_date')
    expiry = datetime.strptime(expiry, "%Y-%m-%dT%H:%M:%S.%f")
    date = expiry.strftime('%Y-%m-%d')
    time = expiry.strftime('%H:%M:%S')
    msg = Message('Expiration of a project', sender='Time Master oyebamijimustapha44@gmail.com', recipients=[email])
    msg.body = "Hello {},\nYour project {} will soon expire on {} at {}. \
It's high time you completed the project".format(name, p_name, date, time)
    try:
        mail.send(msg)
        return jsonify({'status': 'success', 'description': 'Email sent'}), 201
    except:
        pass
    return jsonify({'status': 'error', 'description': 'Email not sent'}), 200

@notification.route('task/expire', methods=['POST'], strict_slashes=False)
def expire_task():
    """Mail for task expiration"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description='No first_name')
    if 'project_name' not in request.get_json():
        abort(400, description='No project_name')
    if 'task_name' not in request.get_json():
        abort(400, description='No task_name')
    if 'email' not in request.get_json():
        abort(400, description='No email')
    if 'expiry_date' not in request.get_json():
        abort(400, description='No expiry date')
    data = request.get_json()
    name = data.get('name')
    task = data.get('task_name')
    email = data.get('email')
    p_name = data.get('project_name')
    expiry = data.get('expiry_date')
    expiry = datetime.strptime(expiry, "%Y-%m-%dT%H:%M:%S.%f")
    date = expiry.strftime('%Y-%m-%d')
    time = expiry.strftime('%H:%M:%S')
    msg = Message('Expiration of a task', sender='Time Master oyebamijimustapha44@gmail.com', recipients=[email])
    msg.body = "Hello {},\nYour task {} under the project {} will soon expire on {} at {}. \
It's high time you completed the task so you could complete the project".format(name, task, p_name, date, time)
    try:
        mail.send(msg)
        return jsonify({'status': 'success', 'description': 'Email sent'}), 201
    except:
        pass
    return jsonify({'status': 'error', 'description': 'Email not sent'}), 200
