import time
from app import worker

print("Worker starting...")
worker.start()
print("Worker started. Processing jobs for 5 minutes...")

# 5 minute tak chalao taaki job complete ho sake
time.sleep(300) 
print("Worker finished.")
