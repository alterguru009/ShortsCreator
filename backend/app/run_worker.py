import time
import json
import uuid
from app import db, worker

print("Initializing local SQLite database...")
db.init_db()

print("Reading job.json...")
with open("job.json", "r") as f:
    job_data = json.load(f)

print("Creating local job...")
job_id = db.create_job(job_data, "Daily AI Video")
print(f"Job created with ID: {job_id}")

print("Enqueueing job...")
worker.enqueue(job_id)

print("Worker starting...")
worker.start()

print("Worker started. Processing jobs for 10 minutes...")
time.sleep(600)
print("Worker finished.")
