#!/usr/bin/env python
import settings
from core.views import *
from flask import send_from_directory

@app.route('/htdocs/<path:filename>')
def htdocs(filename):
    return send_from_directory(app.root_path + '/../htdocs/', filename)

if __name__ == '__main__':
    app.run()
