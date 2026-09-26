import time
import json
import uuid
from app import db, worker

print("Initializing local SQLite database...")
db.init_db()

print("Reading job.json...")
with open("job.json", "r") as f:
    job_data = json.load(f)

job_id = "job_" + str(uuid.uuid4())[:12]
print(f"Creating local job {job_id}...")

# db.py ke andar create_job function ko dhundhein, agar naam alag hai toh badal lein
# Yeh function API router bhi use karta hai
db.create_job(job_id, "Daily AI Video", json.dumps(job_data))

print("Enqueueing job...")
worker.enqueue(job_id)

print("Worker starting...")
worker.start()

print("Worker started. Processing jobs for 10 minutes...")
time.sleep(600)
print("Worker finished.")
