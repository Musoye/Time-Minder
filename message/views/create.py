#!/usr/bin/python3
""" Create for account confirmation and changing password """
from models.user import User
from models import storage
from message.views import notification, mail
from flask import jsonify, abort, request
from flask_mail import Message



@notification.route('/register', methods=['POST'])
def create_accout():
    """Mail for creation of a new account"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'first_name' not in request.get_json():
        abort(400, description='No first_name')
    if 'email' not in request.get_json():
        abort(400, description='No email')
    if 'last_name' not in request.get_json():
        abort(400, description='No last_name')
    data = request.get_json()
    name = data.get('first_name')
    email = data.get('email')
    l_name = data.get('last_name')
    msg = Message('Time Master', sender='oyebamijimustapha44@gmail.com', recipients=[email])
    msg.body = '''Hello {name} {l_name},\nYou have take a new step in the mangement of your \
        life. I cant't wait to see you flourish'''.format(name, l_name)
    try:
        mail.send(msg)
        return jsonify({'status': 'sent', 'description': 'Email sent'}), 201
    except:
        pass
    return jsonify({'status': 'error', 'description': 'Email not sent'}), 200

@notification.route('/password', methods=['POST'])
def change_password():
    """Mail for changing of passsword"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'first_name' not in request.get_json():
        abort(400, description='No first_name')
    if 'email' not in request.get_json():
        abort(400, description='No email')
    if 'password' not in request.get_json():
        abort(400, description='No password')
    if 'user_id' not in request.get_json():
        abort(400, description='No user_id')
    data = request.get_json()
    user_id = data.get('user_id')
    user = storage.get(User, user_id)
    if user is None:
        abort(400, description='This user does not exist')
    password = data.get('password')
    user.password = password
    user.save()
    name = data.get('first_name')
    email = data.get('email')
    msg = Message('Time Master', sender='oyebamijimustapha44@gmail.com', recipients=[email])
    msg.body = "Hello {},\nThis is to inform you that your password has been changed sucessfully\
        if you are not the one contact the admin email mmusoye@gmail.com".format(name)
    try:
        mail.send(msg)
        return jsonify({'status': 'sent', 'user_id': user_id, 'description': 'Email sent'}), 201
    except:
        pass
    return jsonify({'status': 'error', 'description': 'Email not sent'}), 200

@notification.route('/unsub', methods=['POST'])
def change_email_subscription():
    """Mail for changing subscription to false"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, description='No user_id')
    data = request.get_json()
    user_id = data.get('user_id')
    user = storage.get(User, user_id)
    if user is None:
        abort(400, description='This user does not exist')
    user.is_suscribe = False
    user.save()
    return jsonify({'status': 'success'}), 201
