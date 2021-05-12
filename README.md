# Flask recipe by Eduardo Rodríguez

The purpose is create 6 services: Login, Logout, a CRUD + Tests and api documentation like swagger.

## Installation steps:

1. Create virtual env: `python3 -m venv venv`.
2. Activate virtual env: `. venv/bin/activate`.
3. Install dependencies: `pip3 install -r requirements.txt`.
4. Install project in editable mode: `pip3 install -e .`.
5. Set the `.env` values.
6. I didnt used alembic in this stage so to create the tables and seed the data we will just do the following:
```
$ python3
>>> from flaskr.db import engine
>>> from flaskr.models import Base
>>> from flaskr.seed import run_seed
>>> Base.metadata.create_all(engine)
>>> run_seed()
```

## Run dev server:
- Run the `flask run` command.
