from fastapi import HTTPException
from typing import List, Dict
from database.db import db
from core.logger import log

class UserService:

    @staticmethod
    def register_user(username: str, public_key: str) -> Dict:
        log.info(f"Attempting registration for: {username}")
        
        if not username.strip():
            log.warning("Registration failed: Empty username")
            raise HTTPException(status_code=400, detail="Username cannot be empty")

        if not public_key.strip():
            log.warning("Registration failed: Empty public key")
            raise HTTPException(status_code=400, detail="Public key cannot be empty")

        if db.user_exists(username):
            log.warning(f"Registration failed: User '{username}' already exists")
            raise HTTPException(
                status_code=400, detail=f"Username '{username}' already registered."
            )

        db.add_user(username, public_key)

        return {
            "status": "success",
            "message": f"User '{username}' registered successfully",
            "username": username,
        }

    @staticmethod
    def get_public_key(username: str) -> Dict:
        log.debug(f"Fetching public key for: {username}")
        public_key = db.get_public_key(username)

        if public_key is None:
            log.warning(f"User not found: {username}")
            raise HTTPException(status_code=404, detail=f"User '{username}' not found.")

        return {"username": username, "public_key": public_key}

    @staticmethod
    def get_all_users() -> List[Dict]:
        log.debug("Fetching all users")
        return [{"username": username} for username in db.get_all_usernames()]

    @staticmethod
    def get_stats() -> Dict:
        log.debug("Fetching stats")
        return {"registered_users": db.count_users()}


user_service = UserService()
