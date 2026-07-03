from flask import Blueprint, request, jsonify, abort
from pydantic import ValidationError

from app.models import db, Question

from app.schemas.questions import QuestionCreate

from app.contracts import *


questions_bp = Blueprint('questions', __name__)


@questions_bp.route('/', methods=['GET', 'POST'])
def questions():
    if request.method == "GET":
        return 'List of questions'
    if request.method == "POST":
        try:
            raw = request.get_json(silent=False)
        except Exception as e:
            return jsonify(ErrorResponse(error="JSON is not valid").model_dump()), 400

        if not raw:
            return jsonify(ErrorResponse(error="No data").model_dump()), 400

        try:
            data = QuestionCreate.model_validate(raw)
            question = Question(**data.model_dump())
            db.session.add(question)
            db.session.commit()

            return jsonify(QuestionResponse.model_validate(question).model_dump()), 201

        except ValidationError as e:
            return jsonify(ErrorResponse(error="Data is not valid").model_dump()), 400




@questions_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def question(id):
    if request.method == "GET":
        return f'Question {id}'
    if request.method == "PUT":
        return f'Update question {id}'
    if request.method == "DELETE":
        return f'Delete question {id}'