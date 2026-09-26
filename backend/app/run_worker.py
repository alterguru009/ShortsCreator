import sys
import json
import static_ffmpeg
from app import db
from app.pipeline import orchestrator
from app.upload_youtube import upload_to_youtube
from app.config import settings

print("Initializing local SQLite database...")
db.init_db()

print("Setting up FFmpeg...")
static_ffmpeg.add_paths(weak=True)

print("Reading job.json...")
with open("job.json", "r") as f:
    job_data = json.load(f)

print("Creating local job...")
job_id = db.create_job(job_data, "Daily AI Video")
print(f"Job created with ID: {job_id}")

print("Running job directly (is process mein 5-10 minute lag sakte hain)...")
try:
    result = orchestrator.run_job(job_id)
    print("Job completed successfully!")
    
    # Upload to YouTube
    print("Uploading to YouTube...")
    video_path = settings.job_dir(job_id) / "short.mp4"
    title = result.get("title", "AI Pulse Daily")
    description = result.get("description", "Daily AI updates")
    tags = result.get("hashtags", [])
    
    if video_path.exists():
        upload_to_youtube(video_path, title, description, tags)
    else:
        print("Video file not found. Skipping upload.")
        
except Exception as e:
    print(f"ERROR OCCURRED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
