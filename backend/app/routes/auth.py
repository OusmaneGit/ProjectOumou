from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from app.services.auth_service import register_user, authenticate_user, refresh_token
from app.utils.exceptions import APIException

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user = register_user(data)
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user.to_dict()
        }), 201
    except APIException as e:
        return jsonify({'message': e.message}), e.status_code

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = authenticate_user(data['email'], data['password'])
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user.to_dict()
        })
    except APIException as e:
        return jsonify({'message': e.message}), e.status_code

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = refresh_token(current_user)
    return jsonify({'access_token': new_token})