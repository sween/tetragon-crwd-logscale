#!/usr/bin/env python

import json
import time
import os
import sys
import requests
import socket
from datetime import datetime
from humiolib.HumioClient import HumioIngestClient


# Required for CRWD Data Source
today = datetime.now()
fqdn = socket.getfqdn()
input_string = sys.stdin.read()
input_json = json.loads(input_string)


payload = [
    {
        "tags": {
            "host": fqdn,
            "source": "irislogd"
        },
            "events": [
            {
                "timestamp": today.isoformat(sep='T',timespec='auto') + "Z",
                "attributes": input_json
            }
        ]
    }
]

file1 = open('/tmp/log.log', 'w')

 
# Writing a string to file
file1.write(input_string)


client = HumioIngestClient(
    base_url= "https://cloud.community.humio.com",
    ingest_token= "6d8e981f-928c-4add-8acf-81c9a5dbb512" # os.environ["CS_LOGSCALE_APIKEY"]
)

ingest_response = client.ingest_json_data(payload)
print(ingest_response)

