import bottle
from bottle import auth_basic, route, run, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from model import Base
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = engine = create_engine(
    '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    ),
    echo=settings.SQLALCHEMY['debug']
)
session_local = sessionmaker(
    bind=engine,
    autoflush=settings.SQLALCHEMY['autoflush'],
    autocommit=settings.SQLALCHEMY['autocommit']
)

def setup_routes():
     bottle.route('/pop/<pop_id>', ['GET', 'DELETE'], crud)
     bottle.route('/pop/<pop_name>/<pop_color>', ['PUT'], insert_entry)
     bottle.route('/pop/<pop_id>/<pop_name>/<pop_color>', ['POST'], update_entry)

def is_authenticated_user(user, password):
    # You write this function. It must return
    # True if user/password is authenticated, or False to deny access.
	if user == 'user' and password == 'pass':
		return True
	return False

def get_strategy(db):
     return Raw(db)

@route('/')
def hello(db):
	return {"hello": "world"}

@route('/pop')
@auth_basic(is_authenticated_user)
def get_all(db):
    strategy = get_strategy(db)
    return strategy.all()

@route('/pop/<pop_id>')
@auth_basic(is_authenticated_user)
def crud(db, pop_id):
    strategy = get_strategy(db)
    if request.method == 'GET':
        return strategy.filter_by(pop_id)
    
    return strategy.delete_by(pop_id)

@route('/pop/<pop_name>/<pop_color>')
@auth_basic(is_authenticated_user)
def insert_entry(db, pop_name, pop_color):
    strategy = get_strategy(db)
    return strategy.insert_entry(pop_name, pop_color)

@route('/pop/<pop_id>/<pop_name>/<pop_color>')
@auth_basic(is_authenticated_user)
def update_entry(db, pop_id, pop_name, pop_color):
    strategy = get_strategy(db)
    return strategy.update_entry(pop_id, pop_name, pop_color)

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=False, create_session = session_local))

setup_routes()

run(host='0.0.0.0', port=8000,debug=True)