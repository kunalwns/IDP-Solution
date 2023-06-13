import requests
from config import *
import json
 
def call_api_get_data(file_location,question_set):

    print("tarun")
     
    url = "https://api.lazarusforms.com/api/rikai"  

    payload = question_set
    print(question_set)
    files=[('file',('file_name',open(file_location,'rb'),'application/octet-stream'))]

    headers = {
    'orgId': ORG_ID,
    'authKey': AUTH_KEY
    }
    print("kumar tarun") 
    print(payload) 
    try:
        response = requests.post(url, headers=headers, data=payload, files=files)  
        print(response.json())
        return response.json()
        
    except Exception as e:
        print("Error")
        print(str(e)) 
     

def call_invoice_api_get_data(file_location,question_set):

    print("Calling INvoice")
     
    url = "https://api.lazarusforms.com/api/forms/invoices"  

    payload = {}
     
    files=[('file',('file_name',open(file_location,'rb'),'application/octet-stream'))]

    headers = {
    'orgId': ORG_ID,
    'authKey': AUTH_KEY
    }
     
    try:
        response = requests.post(url, headers=headers, data=payload, files=files)  
        print(response.json())
        return response.json()
        
    except Exception as e:
        print("Error")
        print(str(e)) 