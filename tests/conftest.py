# conftest.py Usually run before test_routes.py run?
# We do not run migration with test database

import pytest
from app import create_app 
from app.db import db
from flask.signals import request_finished 
from dotenv import load_dotenv 
import os
from app.models.cat import Cat


# python-detenv
load_dotenv() # Before we can use our environment variables, we need to invoke the load_dotenv function that we imported.

@pytest.fixture # Fixtures Like helper function
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI') # Connect to Test Database
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()  # Create all databases
        yield app # like return app, it could resume after test finishes run.
                    # If uses run, the folloing will not run. 
                    # It remember when we end in the function
                    # Return and come back

    with app.app_context(): # Remove all database tables
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_cat(app):
    # Arrange
    cat = Cat(
        name="Foo",
        color="black",
        personality='sleepy'
    )


    db.session.add(cat)
    db.session.commit()
    return cat
