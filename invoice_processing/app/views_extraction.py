from django.shortcuts import render
from django.conf import settings 
 
from .libs.service_lib.prop_doc_info import Prop_Doc_Info
from .libs.service_lib.srv_process_info import Srv_Process_Info
from .libs.service_lib.srv_doc_info import Srv_Doc_Info
import os

# Lib References


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
    print("tarun kumar")
    print(user_id)
    if(user_id != "" and company_id != ""): 
       
        obj_srv_doc_info = Srv_Doc_Info()
        results = obj_srv_doc_info.List_Ready_To_Process_Docs(user_id,company_id)
        
        result =  {"status" : "1", "message" : "" ,"result" : results }    
        return render(request, 'views/extraction/index.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')


def processed(request):

    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""): 
         
        obj_srv_processed_doc  = Srv_Process_Info()
        results = obj_srv_processed_doc.Get_Processed_Document(user_id,company_id)
        print(results)
        result =  {"status" : "1", "message" : "" ,"result" : results }
        return render(request, 'views/extraction/processed.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')


def  detail(request,id):
    company_id = get_company_id(request)
    user_id = get_user_id(request)

    document_root = os.path.join(settings.STATIC_FILE_HOST,company_id)
    print(document_root)
    return render(request, 'views/extraction/detail.html',{'process_id':str(id), "doc_root_path" : document_root})
     
