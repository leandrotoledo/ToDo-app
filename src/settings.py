#!/usr/bin/env python
from core.models import db

db.bind('sqlite', 'db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
