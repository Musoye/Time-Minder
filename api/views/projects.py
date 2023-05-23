#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users"""
from models.project import Project
from models import storage
from api.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/projects', methods=['GET'], strict_slashes=False)
def get_projects():
    """
    Retrieves the list of all project objects
    or a specific project
    """
    all_users = storage.all(Project).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/projects/<project_id>', methods=['GET'], strict_slashes=False)
def get_project(project_id):
    """ Retrieves a project """
    user = storage.get(Project, project_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/projects/<project_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_project(project_id):
    """
    Deletes a user Object
    """

    user = storage.get(Project, project_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/projects', methods=['POST'], strict_slashes=False)
def post_project():
    """
    Creates a project
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    instance = Project(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/projects/<project_id>', methods=['PUT'], strict_slashes=False)
def put_project(project_id):
    """
    Updates a project
    """
    user = storage.get(Project, project_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['user_id', 'id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
