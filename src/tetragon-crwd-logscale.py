import sys
import time
import json
import os
import socket
import subprocess
from datetime import datetime
from humiolib.HumioClient import HumioIngestClient

def send_siem(line):
    # Do something with the line
    print(line.decode())
    # Required for CRWD Data Source
    today = datetime.now()
    fqdn = socket.getfqdn()
    input_json = json.loads(line.decode())


    payload = [
        {
            "tags": {
                "host": fqdn,
                "source": "tetragon"
            },
                "events": [
                {
                    "timestamp": today.isoformat(sep='T',timespec='auto') + "Z",
                    "attributes": input_json
                }
            ]
        }
    ]


    client = HumioIngestClient(
        base_url= "https://cloud.community.humio.com",
        ingest_token = os.environ["CS_LOGSCALE_APIKEY"])

    ingest_response = client.ingest_json_data(payload)
    print(ingest_response)

    
def tail_file(filename):
    process = subprocess.Popen(["tail", "-f", filename], stdout=subprocess.PIPE)
    while True:
        line = process.stdout.readline()
        if not line:
            break
        send_siem(line)
  
tail_file("/var/log/tetragon/tetragon.log")