from django.shortcuts import render

from .libs.service_lib.srv_doc_info import Srv_Doc_Info
from .libs.service_lib.prop_doc_info import Prop_Doc_Info
# Lib References
from .libs.service_lib.srv_process_info import Srv_Process_Info
from .libs.service_lib.srv_config_info import Srv_Config_Info
import os
from django.conf import settings 
import json
import pandas


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


# Create your views here.
def index(request):
    
    print(request)
    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""):  
        obj_srv_doc_info = Srv_Doc_Info()
        results = obj_srv_doc_info.List_docs(user_id,company_id)        
        result =  {"status" : "1", "message" : "" ,"result" : results }        
        return render(request, 'views/documents/index.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')


def upload(request):

    obj_srv_config_info = Srv_Config_Info() 

    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""):         
        lst_layouts = obj_srv_config_info.Get_All_Configs(company_id)  
        return render(request, 'views/documents/upload.html',{'lst_layouts':lst_layouts})
    else:
        return render(request, 'views/login.html')

def check_api_response(request): 

    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""):        
         
        return render(request, 'views/documents/chek_api_questions.html')
    else:
        return render(request, 'views/login.html')


def processed(request):
    company_id = get_company_id(request)
    user_id = get_user_id(request)
    obj_srv_processed_doc  = Srv_Process_Info()
    results = obj_srv_processed_doc.Get_Processed_Media(user_id,company_id)
    print(results)
    result =  {"status" : "1", "message" : "" ,"result" : results }
    return render(request, 'views/documents/processed.html',{'doc_list':result})

 