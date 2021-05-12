from marshmallow import Schema, fields
from flaskr.models import User
from flaskr.db import session

class LoginRequestSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserSchema(Schema):
    id = fields.Int()
    fullname = fields.Str()
    username = fields.Str()