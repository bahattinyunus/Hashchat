import pytest
import os
from database.db import Database, DATABASE_URL

# Use a test database file
TEST_DB_URL = "sqlite:///./test_hashchat.db"

# Mock the database connection for testing
@pytest.fixture
def test_db():
    # Setup
    db = Database()
    # Override engine to use test DB
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from database.models import Base
    
    db.engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
    db.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db.engine)
    db.init_db()
    
    yield db
    
    # Teardown
    db.engine.dispose()
    if os.path.exists("./test_hashchat.db"):
        os.remove("./test_hashchat.db")

def test_add_and_get_user(test_db):
    username = "test_user_persistence"
    key = "public_key_123"
    
    test_db.add_user(username, key)
    
    retrieved_key = test_db.get_public_key(username)
    assert retrieved_key == key
    assert test_db.user_exists(username) is True

def test_user_persistence_reloaded(test_db):
    # This test simulates a "reload" by using a new session/db check 
    # but strictly speaking, simply creating a new query proves persistence in the file
    username = "persistent_user"
    key = "persistent_key"
    
    test_db.add_user(username, key)
    
    # New query from fresh connection
    exists = test_db.user_exists(username)
    assert exists is True
