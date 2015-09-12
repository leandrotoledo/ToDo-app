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
    def test_1_add_note(self):
        note = Note(annotation='This is an annotation')
        db.commit()

        self.assertEquals(note.id, 1)
        self.assertEquals(note.annotation, 'This is an annotation')

    @db_session
    def test_2_get_note(self):
        note = Note[1]

        self.assertEquals(note.id, 1)
        self.assertEquals(note.annotation, 'This is an annotation')

    @db_session
    def test_3_update_note(self):
        note = Note[1]
        note.annotation = 'This is a new annotation'
        db.commit()

        self.assertEquals(note.id, 1)
        self.assertEquals(note.annotation, 'This is a new annotation')

    @db_session
    def test_4_delete_note(self):
        note = Note[1]
        note.delete()

        self.assertEquals(Note.get(id=1), None)
