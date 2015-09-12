**********************
Setting up environment
**********************

Getting the code
================

`$ git clone https://github.com/leandrotoledo/ToDo-app.git`

`$ cd ToDo-app`

On Ubuntu 14.04
===============

1. Python 3 Virtual Environment
-------------------------------
`$ pyvenv-3.4 --without-pip venvdir`

`$ source venvdir/bin/activate`

`$ curl https://bootstrap.pypa.io/get-pip.py | venvdir/bin/python`

2. Python Dependencies
----------------------
`$ pip install -r requirements.txt`

3. Bower Dependencies
---------------------
`$ bower install`

Running tests
=============
`$ make test`

Running app
===========
`$ python src/main.py`

`http://127.0.0.1:5000/htdocs/index.html`

************
Useful links
************

- `PonyORM <http://doc.ponyorm.com>`_
- `Flask <http://flask.pocoo.org/docs/>`_
- `Flask-RESTful <https://flask-restful.readthedocs.org>`_
