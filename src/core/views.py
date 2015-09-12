#!/usr/bin/env python
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

class NotesResource(Resource):
    @db_session
    def post(self):
        annotation = request.form['annotation']
        note = Note(annotation=annotation)

        db.commit()

        return note.to_dict(), 201

api.add_resource(NotesResource, '/notes')
api.add_resource(NoteResource, '/note/<note_id>')
