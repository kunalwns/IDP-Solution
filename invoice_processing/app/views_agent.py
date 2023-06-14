from django.shortcuts import render

 
# Lib References
from .libs.service_lib.srv_agent_docs import srv_agent_docs
 
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
    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""): 
        result =  {"status" : "1", "message" : "" ,"result" : [] }        
        return render(request, 'views/agent/index.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')


def check_question(request):
    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""): 
        result =  {"status" : "1", "message" : "" ,"result" : [] }        
        return render(request, 'views/agent/check_api.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')


def get_file_list(company_id,config_id,doc_id):
    src_location_dir = os.path.join(settings.DOC_IMAGE_LOCATION_DIR,company_id,config_id,"processed",doc_id,"images")
    dir_list = os.listdir(src_location_dir)
    return dir_list


def document(request,id): 
    company_id = get_company_id(request)
    user_id = get_user_id(request)
    document_id = str(id)
    config_id = ""
    print("document id " + document_id)
    CONFIDENCE_LIMIT = settings.THRESOLD_CONFIDENCE
    if(user_id != "" and company_id != ""):  
        obj_srv_agent_docs = srv_agent_docs()  
        doc_info = obj_srv_agent_docs.get_document_detail_by_id(document_id)
        print(doc_info)
        dict_item = dict(doc_info[0].items())
        file_name = dict_item["doc_name"]
        config_id = dict_item["config_id"]

        # lst_pages = get_file_list(company_id,config_id,document_id)
         
        root_page_path = os.path.join(settings.STATIC_FILE_HOST,company_id,config_id) 
        result =  {"status" : "1", "message" : "" ,"result" : [],"root_page_path" : root_page_path, "document_id" : document_id, "config_id" : config_id,"CONFIDENCE_LIMIT" : CONFIDENCE_LIMIT, "file_name" : file_name }        
        
        if(1==2):
            return render(request, 'views/agent/business_case.html', result)
        else:
            return render(request, 'views/agent/docs.html', result)
         
    else:
        return render(request, 'views/login.html')



 
