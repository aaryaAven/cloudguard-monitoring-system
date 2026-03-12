**☁️ CloudGuard – Cloud Log Monitoring & Alerting System**

CloudGuard is a Python-based monitoring tool that simulates how cloud infrastructure monitoring systems detect issues in server logs.
It analyzes log files, detects warnings and errors, sends real-time alerts, and displays them on a web dashboard.

The application is also containerized using Docker, making it easy to deploy and run in different environments.

**📌 Features**

📄 Log Monitoring – Continuously reads server log files

⚠️ Error & Warning Detection – Identifies abnormal log entries

🚨 Alert System – Sends real-time alerts when issues are detected

📊 Web Dashboard – Displays detected alerts on a monitoring dashboard

🐳 Docker Support – Application can run inside a container

⚙️ Automation – Automatically analyzes logs and triggers alerts

**🏗️ System Architecture**

Server Activity
↓
Log Generator
↓
server.log
↓
Log Analyzer
↓
Alert System
↓
Discord Notification
↓
CloudGuard Dashboard

**🗂️ Project Structure**

cloudguard
│
├── analyzer
│ └── log_analyzer.py
│
├── alerts
│ └── email_alert.py
│
├── dashboard
│ ├── app.py
│ └── templates
│ └── dashboard.html
│
├── logs
│ └── server.log
│
├── log_generator.py
├── Dockerfile
├── requirements.txt
└── README.md

**⚙️ Installation & Setup**
**1. Clone the Repository**

git clone https://github.com/yourusername/cloudguard-monitoring-system.git

cd cloudguard-monitoring-system

**2. Install Dependencies**

pip install -r requirements.txt

**3. Start the Dashboard**

python dashboard/app.py

Open in browser:

http://localhost:5000

**4. Start Log Generator**

Open another terminal and run:

python log_generator.py

This will simulate server logs.

**5. Start Log Analyzer**

Open another terminal and run:

python -m analyzer.log_analyzer

Now CloudGuard will detect warnings and errors automatically.

**🐳 Running with Docker**

Build Docker image:

docker build -t cloudguard .

Run container:

docker run -p 5000:5000 cloudguard

Open browser:

http://localhost:5000

**🖥️ Example Alerts**

WARNING: High memory usage
ERROR: Database connection failed

These alerts will appear on the dashboard and be sent to the configured notification system.

**🛠️ Technologies Used**

Python

Flask

Docker

Log Monitoring Concepts

Web Dashboard Development

**📚 Skills Demonstrated**

This project demonstrates:

Log Monitoring

Automation

DevOps Concepts

Containerization

Backend Development

Alert Systems

**🚀 Future Improvements**

Real-time charts for log statistics

Kubernetes deployment

Integration with cloud monitoring services

Advanced log filtering

Role-based dashboard access

**👨‍💻 Author**

Aarya Kshirsagar
