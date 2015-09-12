#!/usr/bin/env python
import json
from flask import Flask, request
from flask_restful import Resource, Api
from pony.orm import db_session
from .models import db, Note

app = Flask(__name__)
api = Api(app)

class NoteResource(Resource):
    @db_session
    def get(self, note_id):
        return {'data': Note[note_id].to_dict()}

    @db_session
    def put(self, note_id):
        note = Note[note_id]
        note.annotation = request.json['annotation']

        db.commit()

        return {'data': note.to_dict()}

    @db_session
    def delete(self, note_id):
        note = Note[note_id]
        note.delete()

        db.commit()

        return '', 204

class NotesResource(Resource):
    @db_session
    def post(self):
        note = Note(annotation=request.json['annotation'])

        db.commit()

        return note.to_dict(), 201

api.add_resource(NotesResource, '/notes')
api.add_resource(NoteResource, '/note/<note_id>')
