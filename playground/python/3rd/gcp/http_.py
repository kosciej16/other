import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Replace these variables with your values
PROJECT_ID = "theta-marking-348120"
TOPIC_NAME = "kosciej-topic"
SERVICE_ACCOUNT_FILE = "/home/kosciej/.gcp.json"

# Initialize the credentials object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Define the Pub/Sub endpoint
url = f"https://pubsub.googleapis.com/v1/projects/{PROJECT_ID}/topics/{TOPIC_NAME}:publish"
#
# # Define the message to publish
message_data = {
    "messages": [
        {
            "data": "SGVsbG8sIFdvcmxkIQ=="  # This is "Hello, World!" encoded in base64
        }
    ]
}
#
# # Acquire a token using the service account credentials
authed_session = Request()
credentials.refresh(authed_session)
headers = {"Authorization": f"Bearer {credentials.token}", "Content-Type": "application/json"}
#
# # Send the request
response = requests.post(url, headers=headers, json=message_data)
#
# # Check the response
if response.status_code == 200:
    print("Message published successfully.")
else:
    print("Failed to publish message:", response.status_code, response.text)
