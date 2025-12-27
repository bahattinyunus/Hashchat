import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

try:
    print("Attempting to import database.db...")
    from database.db import db
    print("Successfully imported db instance.")
    print(f"Engine: {db.engine}")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()
