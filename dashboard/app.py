from flask import Flask, render_template

app = Flask(__name__)

LOG_FILE = "logs/server.log"

@app.route("/")
def dashboard():

    alerts = []

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    for log in logs:
        if "ERROR" in log or "WARNING" in log:
            alerts.append(log.strip())

    return render_template("dashboard.html", alerts=alerts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)