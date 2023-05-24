#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Tasks"""
from models.task import Task
from models import storage
from api.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/tasks', methods=['GET'], strict_slashes=False)
def get_tasks():
    """
    Retrieves the list of all task objects
    """
    all_users = storage.all(Task).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/tasks/<task_id>', methods=['GET'], strict_slashes=False)
def get_task(task_id):
    """ Retrieves a task """
    user = storage.get(Task, task_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/tasks/<task_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_task(task_id):
    """
    Deletes a task Object
    """

    user = storage.get(Task, task_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/tasks', methods=['POST'], strict_slashes=False)
def post_task():
    """
    Creates a task
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")
    if 'project_id' not in request.get_json():
        abort(400, description="Missing project_id")
    if 'status' not in request.get_json():
        abort(400, description="Missing status")

    data = request.get_json()
    if data.get('status') not in ['doing', 'todo', 'done']:
        abort(400, description='The value of status should be doing, todo and done')
    instance = Task(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/tasks/<task_id>', methods=['PUT'], strict_slashes=False)
def put_task(task_id):
    """
    Updates a task
    """
    user = storage.get(Task, task_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['user_id', 'project_id', 'id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
