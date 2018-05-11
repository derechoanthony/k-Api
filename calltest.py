import requests

url = "http://10.0.1.126:3000/api/v1.0/user/list"

headers = {
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIiLCJleHAiOjE1MjE3ODg4NTJ9.OmXwbRrM5PJQm3Bmrk6QMxVB13sBSbjH3sqEDfTr4ls",
    'Cache-Control': "no-cache",
    'Postman-Token': "352048c8-8523-4198-bfe1-51ccb2f3a44a"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
