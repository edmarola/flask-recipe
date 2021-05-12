from flask import Flask, jsonify, abort, make_response, session
from flaskr.schemas import LoginRequestSchema, UserSchema
from webargs.flaskparser import use_args
from flaskr.models import User
from flaskr.db import session as db_session
import bcrypt
import os

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'my-secret-key')
)

@app.route('/auth/login', methods=['POST'])
@use_args(LoginRequestSchema())
def login(args):
    user = db_session.query(User).filter(User.username==args['username']).first()
    if user is None:
        abort(make_response(jsonify(error='Invalid Credentials'), 401))
    else:
        if bcrypt.checkpw(args['password'].encode('utf-8'), user.password.encode('utf-8')):
            session['username'] = args['username']
            return UserSchema().dump(user), 200
        else:
            abort(make_response(jsonify(error='Invalid Credentials'), 401))

@app.route('/auth/logout', methods=['DELETE'])
def logout():
    session.pop('username')
    session.clear()
    return '', 204

# Return validation errors as JSON
@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    """Return JSON instead of HTML for HTTP errors."""
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code