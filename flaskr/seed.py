from flaskr.db import session
from flaskr.models import User

def run_seed():
    try:
        user = User(fullname='Eduardo Rodríguez', username='edmarola', password='1234')
        session.add(user)
        session.commit()
    except:
        session.rollback()
        raise