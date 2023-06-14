from django.shortcuts import render
from django.shortcuts import render 
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import * 
from django.conf import settings 
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view
import os
import json
import uuid
from datetime import datetime
from datetime import datetime,timedelta
import ast
import requests

# Lib References
from .libs.service_lib.srv_agent_docs import srv_agent_docs
 

def get_extention(filename):
    split_tup = os.path.splitext(filename)
    file_extension = split_tup[1]
    return file_extension.replace(".","")

def get_user_id(request):
    user_id = ""
    if 'user_info' in request.session:
        user_id = str(request.session['user_info'][0]["id"])
    else:
        user_id = ""
    return user_id

def get_company_id(request):
    company_id = ""
    if 'user_info' in request.session:
        company_id = str(request.session['user_info'][0]["company_id"])
    else:
        company_id = ""
    return company_id


  
@api_view(["POST"])  
def get_document_field_list(request):
    user_id = get_user_id(request)
    organization_id = get_company_id(request)

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    config_id = dictData["config_id"]   
    
    try: 
        obj_srv_agent_doc = srv_agent_docs()
        data_result = obj_srv_agent_doc.get_document_fields(organization_id,config_id)  
        
        result =  {"field_list" : data_result ,"status" : "1", "message" : "Fetched Record successfully", "error" : "0" } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)


def fetch_extracted_json(company_id,config_id,document_id):
    # obj_json = [{"answer" : "Tarun Kumar","confidence" : "10","question" : "Who is the employeer"},    
    # {"answer" : "920564349498","confidence" : "90","question" : "Who is the Telephone Number"},
    # {"answer" : "Claim Form","confidence" : "20","question" : "What type of document is"}]
    json_file_path =  os.path.join(settings.DOC_IMAGE_LOCATION_DIR,company_id,config_id,"processed",document_id,"json")
    dir_list = os.listdir(json_file_path)
    # JSON file
    f = open (os.path.join(json_file_path,dir_list[0]), "r")
    
    # Reading from file
    json_output = json.loads(f.read()) 
    # Closing file
    f.close()
     
    return json_output

def search_price (items,name):
    for keyval in items:
        if name.lower() == keyval['question'].lower():
            return keyval




@api_view(["POST"])  
def check_api(request):
    url = "https://api.lazarusforms.com/api/forms/invoices"  
    
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    file_name = dictData["file_name"]   
    question = dictData['question']
  
 
    file_location = os.path.join(settings.DOC_IMAGE_LOCATION_DIR,"dump",file_name)
    payload = {} 
    files=[('file',('file_name',open(file_location,'rb'),'application/octet-stream'))]

    headers = {
    'orgId': settings.ORG_ID,
    'authKey': settings.AUTH_KEY
    } 
     
    try:
        response = requests.post(url, headers=headers, data=payload, files=files)  
        result =  {"api_response" : response.json() ,"status" : "1"}    
        print(response.json())   
 
         
        return JsonResponse(result,safe=False)
        
    except Exception as e:
        print("Error")
        print(str(e)) 


@api_view(["POST"])  
def get_document_field_data(request):
    user_id = get_user_id(request)
    organization_id = get_company_id(request)

    lst_results = []
    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    config_id =  dictData["config_id"]   
    document_id =  dictData["document_id"]  
    
    extracted_json = fetch_extracted_json(organization_id,config_id,document_id)
    print(extracted_json)
    try: 
        
        result =  {"data" : extracted_json ,"status" : "1", "message" : "Fetched Record successfully", "error" : "0" } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)

 

