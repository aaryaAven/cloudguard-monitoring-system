import time
from alerts.email_alert import send_email_alert

LOG_FILE = "logs/server.log"

def analyze_logs():
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    for log in logs:
        if "ERROR" in log:
            print("Error detected:", log.strip())
            send_email_alert(log)

        elif "WARNING" in log:
            print("Warning detected:", log.strip())

if __name__ == "__main__":
    while True:
        analyze_logs()
        time.sleep(10)