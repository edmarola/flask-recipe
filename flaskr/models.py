from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import event
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String)
    

def hash_password(mapper, connection, target):
    target.password = bcrypt.hashpw(target.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

event.listen(
    User, 'before_insert', hash_password)