from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from database.models import Base, User
from core.logger import log
from typing import Optional, List

DATABASE_URL = "sqlite:///./hashchat.db"

class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        log.info(f"Database initialized at {DATABASE_URL}")

    def init_db(self):
        Base.metadata.create_all(bind=self.engine)
        log.info("Database tables created.")

    def get_session(self) -> Session:
        return self.SessionLocal()

    def add_user(self, username: str, public_key: str) -> None:
        session = self.get_session()
        try:
            new_user = User(username=username, public_key=public_key)
            session.add(new_user)
            session.commit()
            log.info(f"User added: {username}")
        except Exception as e:
            log.error(f"Error adding user: {e}")
            session.rollback()
            raise
        finally:
            session.close()

    def get_public_key(self, username: str) -> Optional[str]:
        session = self.get_session()
        try:
            user = session.query(User).filter(User.username == username).first()
            return user.public_key if user else None
        finally:
            session.close()

    def user_exists(self, username: str) -> bool:
        session = self.get_session()
        try:
            return session.query(User).filter(User.username == username).first() is not None
        finally:
            session.close()

    def get_all_usernames(self) -> List[str]:
        session = self.get_session()
        try:
            users = session.query(User).all()
            return [user.username for user in users]
        finally:
            session.close()

    def count_users(self) -> int:
        session = self.get_session()
        try:
            return session.query(User).count()
        finally:
            session.close()

db = Database()
