import sys
import json
from app import db
from app.pipeline import orchestrator

print("Initializing local SQLite database...")
db.init_db()

print("Reading job.json...")
with open("job.json", "r") as f:
    job_data = json.load(f)

print("Creating local job...")
job_id = db.create_job(job_data, "Daily AI Video")
print(f"Job created with ID: {job_id}")

print("Running job directly (is process mein 5-10 minute lag sakte hain)...")
try:
    orchestrator.run_job(job_id)
    print("Job completed successfully!")
except Exception as e:
    print(f"ERROR OCCURRED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
