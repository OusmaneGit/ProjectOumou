from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.course_service import create_course, get_course, update_course
from app.services.course_service import add_variant, add_variant_item
from app.utils.decorators import teacher_required
from app.utils.exceptions import APIException

course_bp = Blueprint('course', __name__)

@course_bp.route('', methods=['POST'])
@jwt_required()
@teacher_required
def create_course_route():
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        course = create_course(current_user_id, data)
        return jsonify(course.to_dict()), 201
    except APIException as e:
        return jsonify({'message': e.message}), e.status_code

@course_bp.route('/<int:course_id>', methods=['GET'])
def get_course_route(course_id):
    try:
        course = get_course(course_id)
        return jsonify(course.to_dict(with_variants=True))
    except APIException as e:
        return jsonify({'message': e.message}), e.status_code

@course_bp.route('/<int:course_id>/variants', methods=['POST'])
@jwt_required()
@teacher_required
def add_variant_route(course_id):
    try:
        data = request.get_json()
        variant = add_variant(course_id, data)
        return jsonify(variant.to_dict()), 201
    except APIException as e:
        return jsonify({'message': e.message}), e.status_code

@course_bp.route('/variants/<int:variant_id>/items', methods=['POST'])
@jwt_required()
@teacher_required
def add_variant_item_route(variant_id):
    try:
        file = request.files.get('file')
        data = request.form.to_dict()
        item = add_variant_item(variant_id, data, file)
        return jsonify(item.to_dict()), 201
    except APIException as e:
        return jsonify({'message': e.message}), e.status_code