from flask import Blueprint, request, jsonify
from models.models import db, User
import utils as u

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users/', methods=['GET', 'POST'])
@users_blueprint.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_users(user_id=None):
    users = []
    if not user_id:

        if request.method == 'GET':
            data = User.query.all()
            for user in data:
                users.append(u.make_dict_users(user))
            return jsonify(users)

        elif request.method == 'POST':
            data = request.json
            user = User(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                age=data.get('age'),
                email=data.get('email'),
                role=data.get('role'),
                phone=data.get('phone'),
            )
            db.session.add(user)
            db.session.commit()
            return f"User {data.get('first_name')} {data.get('last_name')} added!", 201
    else:
        try:

            if request.method == 'GET':
                user = User.query.get(user_id)
                data = u.make_dict_users(user)
                return jsonify(data)

            elif request.method == 'PUT':
                data = request.json
                user = User.query.get(user_id)
                user.first_name = data.get('first_name')
                user.last_name = data.get('last_name')
                user.age = data.get('age')
                user.email = data.get('email')
                user.role = data.get('role')
                user.phone = data.get('phone')
                db.session.add(user)
                db.session.commit()
                return f"User with ID: {user_id} overwritten"

            elif request.method == 'DELETE':
                user = User.query.get(user_id)
                db.session.delete(user)
                db.session.commit()
                return f"User with ID: {user.id} deleted", 204

        except AttributeError:
            return f'ID "{user_id}" for offers not found'
