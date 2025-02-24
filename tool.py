import requests
from dotenv import load_dotenv
import os
def getReputation(ip):
    load_dotenv()
    ABUSE_IP_API_KEY= os.getenv('ABUSE_IP_API_KEY')
    url="https://api.abuseipdb.com/api/v2/check"
    body={"ipAddress":ip}
    headers={"Key":ABUSE_IP_API_KEY,"Accept":'application/json'}
    response =requests.get(url=url,params=body,headers=headers)
    return response.text

print(getReputation('92.255.85.107'))