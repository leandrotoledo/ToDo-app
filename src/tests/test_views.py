#!/usr/bin/env python
import unittest
import json
from flask import request
from pony.orm import *
from core.models import db, Note
from core.views import app


class NoteViewTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.bind('sqlite', 'test_views_db.sqlite', create_db=True)
        db.generate_mapping(create_tables=True)

    def setUp(self):
        self.app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        db.drop_all_tables(with_all_data=True)

    @db_session
    def test_add_note(self):
        data = {'annotation': 'This is an annotation'}

        response = self.app.post('/notes', data=data)

        self.assertEqual(response.status_code, 201)

    @db_session
    def test_get_note(self):
        response = self.app.get('/note/1').get_data()
        note = json.loads(response.decode())['data']

        self.assertEqual(note['id'], 1)
        self.assertEqual(note['annotation'], 'This is an annotation')