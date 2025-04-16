import requests
import os

git_user = os.environ.get("GIT_USER")
git_repo = os.environ.get("GIT_REPO")
git_access_token = os.environ.get("GIT_ACCESS_TOKEN")
url = f"https://api.github.com/repos/{git_user}/{git_repo}/dispatches"
print(url)

payload = "{\"event_type\":\"webhook\",\"client_payload\":{\"unit\":false,\"integration\":true}}"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {git_access_token}",
    "User-Agent": "testapp",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.request("POST", url, data=payload, headers=headers)

if response.status_code == 204:
    print("Success")

print(response.status_code)