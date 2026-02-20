from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


app = Flask(__name__)

@app.route('/')
def say():
    url = "https://dugutarithishkumar.atlassian.net/rest/api/3/project"
EMAIL_COM = 
API_TOKEN =  # Please use a new token!

auth = HTTPBasicAuth(EMAIL_COM, API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# I removed the security scheme line so Jira uses the defaults
payload = json.dumps({
  "key": "RITH1",
  "name": "Rithish Project One",
  "projectTypeKey": "business",
  "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking",
  "description": "Creating my first project via Python",
  "leadAccountId": "712020:c3830646-a8ed-413a-9b79-ca3ab3744c49",
  "assigneeType": "PROJECT_LEAD"
})



return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))




if __name__ == '__main__'
    app.run("0.0.0.0")
