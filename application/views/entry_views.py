from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Resource, Namespace, fields
from flask import request, jsonify
from datetime import datetime

from application.models.entry_models import DiaryEntry
from application import db

api = Namespace('diary entry', Description='Operations on entries')


diary = DiaryEntry()


class Entry(Resource):

    @jwt_required
    def get(self, entry_id=None):
        """ get a single diary entry """

        response = diary.get_diary_entry(entry_id)
        return response

    @jwt_required
    def put(self, entry_id):
        """ update a diary entry """

        response = diary.update_diary_entry(entry_id)
        return response

    @jwt_required
    def delete(self, entry_id):
        """ delete diary entry """
        response = diary.delete_diary_entry(entry_id)
        return response


class Entries(Resource):

    @jwt_required
    def post(self):
        """ create diary entry """

        data = request.get_json()
        response = diary.post_diary_entry(data)
        return response

    @jwt_required
    def get(self):
        """ get all diary entries """

        response = diary.get_all_entries()
        return response


api.add_resource(Entries, '/entries')
api.add_resource(Entry, '/entries/<entry_id>')
