# https://github.com/mpetazzoni/sseclient

import json
import pprint
import sseclient
import requests

# curl -N -X POST  \
# -H "Content-Type: application/json" \
# -d '{"query":"大谷翔平はどこに所属していますか？"}' \
# http://localhost:8080/streaming/ask


url = 'http://0.0.0.0:8080/streaming/ask'
query = {"query": "What is the meaning of life?"}
headers = {'Accept': 'text/event-stream'}
response = requests.post(url, stream=True, headers=headers,json = query)
client = sseclient.SSEClient(response)


for event in client.events():
    print(event.data)
    print(type(event.data))
    if event.data != "":
        print(json.loads(event.data))