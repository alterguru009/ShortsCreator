import time
from app import worker, db

print("Initializing database...")
db.init_db()

print("Worker starting...")
worker.start()

print("Worker started. Processing jobs for 5 minutes...")
# 5 minute tak chalao taaki job complete ho sake
time.sleep(600) 
print("Worker finished.")
