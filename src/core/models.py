#!/usr/bin/env python
from pony.orm import *

db = Database()
class Note(db.Entity):
    annotation = Required(str)
