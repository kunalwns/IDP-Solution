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
import uuid
from datetime import datetime
from datetime import datetime,timedelta
import ast
import requests

# Lib References
from .libs.service_lib.srv_extraction_info import Srv_Extraction_Info
from .libs.service_lib.srv_process_info import Srv_Process_Info
from .libs.service_lib.prop_process_info import Prop_Process_Info



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
def run_audio_extraction(request):

    # Get Session Variables
    user_id = get_user_id(request)
    organization_id = get_company_id(request)

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    config_id = ""  
    document_name = dictData["document_name"]
    document_id = dictData["doc_id"]
    
    print(document_name)
    print(document_id)
    try:  
        
        process_uuid = str(uuid.uuid1()) 

        data = {'document_name':document_name, 'document_id':document_id, 'user_id':user_id, "config_id" : config_id, 'organization_id':organization_id, "process_uuid" : process_uuid }

         
        # Save Process Info
        Save_Process(process_uuid,user_id,"3",document_id)

        # CALL PROCESS API TO EXTRACT INFORMATION
        try:
            print("tarun")
            response = requests.post(url = settings.AUDIO_API_LINK, data = data, timeout=2.50)  
            result =  {"status" : "1", "message" : "Request Raised successfully","error" : "0" } 
        except Exception as e:
            result =  {"status" : "0", "message" : str(e), "error" : "1" } 
                 
  
        
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)








@api_view(["POST"])  
def run_extraction(request):

    # Get Session Variables
    user_id = get_user_id(request)
    organization_id = get_company_id(request)

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    config_id = dictData["config_id"]   
    document_name = dictData["document_name"]
    document_id = dictData["doc_id"]
    
    try:  
        
        process_uuid = str(uuid.uuid1())

         
        # Save Process Info
        #Save_Process(process_uuid,user_id,config_id,document_id)

        data = {'document_name':document_name, 'document_id':document_id, 'user_id':user_id, "config_id" : config_id, 'organization_id':organization_id, "process_uuid" : process_uuid,"process_type" : "invoice" }
 
        try:
            print("Raised request")
            response = requests.post(url = settings.PROCESS_API_LINK, data = data, timeout=2.50)  
            result =  {"status" : "1", "message" : "Request Raised successfully","error" : "0" }  
        except Exception as e:
            result =  {"status" : "0", "message" : str(e), "error" : "1" } 
                 
  
        
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)
           

@api_view(["POST"])  
def get_processed_standard_item_detail(request):
    user_id = get_user_id(request)
    organization_id = get_company_id(request)

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    process_id = dictData["process_id"]   
    try:

        obj_srv_process = Srv_Extraction_Info()
        data_result = obj_srv_process.Get_standard_fields(process_id)
        print(data_result)
        result =  {"result" : data_result ,"status" : "1", "message" : "Fetched Record successfully", "error" : "0" } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)


@api_view(["POST"])  
def get_processed_standard_line_item_detail(request):
    user_id = get_user_id(request)
    organization_id = get_company_id(request)

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    process_id = dictData["process_id"]   
    try:

        obj_srv_process = Srv_Extraction_Info()
        data_result = obj_srv_process.Get_standard_lineitems_fields(process_id)
        print(data_result)
        result =  {"result" : data_result ,"status" : "1", "message" : "Fetched Record successfully", "error" : "0" } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)



# Save Process Information
def Save_Process(process_uuid,user_id,config_id,document_id):
    obj_service_process = Srv_Process_Info()
    obj_prop_process_info = Prop_Process_Info()

    now = datetime.now()
    
    obj_prop_process_info.process_uuid = process_uuid
    obj_prop_process_info.doc_id = document_id
    obj_prop_process_info.process_name = 'DOC_' + str(now.strftime("%Y-%m-%d_%H-%M-%S"))
    obj_prop_process_info.process_start_by = "Web"
    obj_prop_process_info.process_start =  None
    obj_prop_process_info.process_end = None
    obj_prop_process_info.process_status = '0'
    obj_prop_process_info.remark = 'Request Raised'
    obj_prop_process_info.error_log = ''
    obj_prop_process_info.user_id = user_id
    obj_prop_process_info.config_id = config_id
    obj_prop_process_info.raised_datetime = str(now.strftime("%Y-%m-%d %H:%M:%S")) 
    obj_service_process.Insert_New_Process(obj_prop_process_info)

     
