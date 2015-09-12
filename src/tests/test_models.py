#!/usr/bin/env python
import unittest
from pony.orm import *
from core.models import db, Note


class NoteModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.bind('sqlite', 'test_models_db.sqlite', create_db=True)
        db.generate_mapping(create_tables=True)

    @classmethod
    def tearDownClass(cls):
        db.drop_all_tables(with_all_data=True)

    @db_session
    def test_add_note(self):
        Note(annotation='This is a test')

        self.assertEquals(Note[1].id, 1)
        self.assertEquals(Note[1].annotation, 'This is a test')

    @db_session
    def test_del_note(self):
        note = Note[1]
        note.delete()

        self.assertEquals(Note.get(id=1), None)
