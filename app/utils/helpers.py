import os
import uuid

def create_session():
    session_id = str(uuid.uuid4())
    path = os.path.join("uploads", session_id)
    os.makedirs(path, exist_ok=True)
    return session_id, path