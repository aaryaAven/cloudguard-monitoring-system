import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1481363855404957709/UtpZ9yBRFxnlnGwUfir6pmW3xz-XR4Vd9nQMyZq0_idsV4qf00W1b5H5iMqdj0Y17E8q"

def send_email_alert(message):

    data = {
        "content": f"🚨 CloudGuard Alert!\nError detected in logs:\n{message}"
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("Discord alert sent!")
    else:
        print("Failed to send alert")