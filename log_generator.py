import time
import random

logs = [
    "INFO: Server started successfully",
    "INFO: User login success",
    "WARNING: High memory usage",
    "ERROR: Database connection failed",
    "INFO: Request processed",
    "ERROR: API timeout"
]

while True:
    with open("logs/server.log", "a") as f:
        log = random.choice(logs)
        f.write(log + "\n")
        print("Generated log:", log)

    time.sleep(5)