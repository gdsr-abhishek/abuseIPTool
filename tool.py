import requests
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import gradio as gr
def getIPSummary(ipData):
    key=os.getenv('OPENAI_API_KEY')
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key= key
)
    prompt = f"""
Summarise abuse IP data and give a verdict on whether the IP address is malicious or not in 250 words:

{ipData}
"""
    result =llm.invoke(prompt)
    return result.content
def getReputation(ip):
    load_dotenv()
    ABUSE_IP_API_KEY= os.getenv('ABUSE_IP_API_KEY')
    url="https://api.abuseipdb.com/api/v2/check"
    body={"ipAddress":ip}
    headers={"Key":ABUSE_IP_API_KEY,"Accept":'application/json'}
    response =requests.get(url=url,params=body,headers=headers).text
    result = getIPSummary(response)
    return result



demo = gr.Interface(fn=getReputation, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    demo.launch()
