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
    
    return json_output['data']

def search_price (items,name):
    for keyval in items:
        if name.lower() == keyval['question'].lower():
            return keyval




@api_view(["POST"])  
def check_api(request):
    url = "https://api.lazarusforms.com/api/rikai"  
    
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    file_name = dictData["file_name"]   
    question = dictData['question']
  
 
    file_location = os.path.join(settings.DOC_IMAGE_LOCATION_DIR,"dump",file_name)
    payload = {"question" : question} 
    files=[('file',('file_name',open(file_location,'rb'),'application/octet-stream'))]

    headers = {
    'orgId': settings.ORG_ID,
    'authKey': settings.AUTH_KEY
    } 
     
    try:
        response = requests.post(url, headers=headers, data=payload, files=files)  
        result =  {"api_response" : response.json() ,"status" : "1"}    
        print(response.json())   

#         result =  {"api_response" : {'data': [{'answer': 'Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan RodríguezJuan Rodríguez  Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez Juan Rodríguez', 'confidence': 0.8322883983800674, 'context': "UnitedHealthcare® Community Plan PRIOR AUTHORIZATION REQUEST FORM Complete ENTIRE form and Fax to: 866-940-7328 Today's Date: SECTION A - PATIENT INFORMATION First Name: Juan Last Name: Rodríguez Address: 1942 Slocum Member ID: 56791377 Rd, Dix Hills, NY City: Dix Hills State: New York Phone 515-739-8864 DOB: 10/17/1992 Primary Insurance: United Select Policy #: 574469812 Zip: 13295 Allergies: Peanuts Group #: 2647 12/19/21 Is the requested medication NEW [' or a CONTINUATION of THERAPYD]? If so, start date: Is this patient currently hospitalized? Yes No SECTION B - PHYSICIAN INFORMATION M.D. D.O. First Name: Samuel Last Name: Charles City: Watertown State:\n", 'question': 'patient name'}], 'documentId': 'file_name', 'endTime': 1685420235303, 'id': '-NWerxcwQ7F86aHj4jjO', 'model': 'RikAI:1.2', 'pages': 1, 'questions': 1, 'startTime': 1685420230307, 'status': 'SUCCESS'}
# ,"status" : "1"}  
         
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

    try: 
        obj_srv_agent_doc = srv_agent_docs()
        data_result = obj_srv_agent_doc.get_document_fields(organization_id,config_id)  
       
        for s in data_result:
            result_output = {}
            dict_item = dict(s.items())             

            json_item = search_price(extracted_json,dict_item["questions"])

            if(json_item):
                round_conf = round(float(json_item["confidence"])*100,0)
                result_output["field_name"] = dict_item["field_name"]
                result_output["key_name"] = dict_item["key_name"]
                result_output["value"] = json_item["answer"]
                result_output["confidence"] = round_conf
                result_output["questions"] = dict_item["questions"]
                print(result_output)
                lst_results.append(result_output) 
            else:
                result_output["field_name"] = dict_item["field_name"]
                result_output["value"] = ""
                result_output["key_name"] = dict_item["key_name"]
                result_output["confidence"] = ""
                result_output["questions"] = dict_item["questions"]
                print(result_output)

        
        print(lst_results)
        result =  {"field_values" : lst_results ,"status" : "1", "message" : "Fetched Record successfully", "error" : "0" } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)

 

