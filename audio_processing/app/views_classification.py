from django.shortcuts import render

from .libs.service_lib.srv_doc_info import Srv_Doc_Info
from .libs.service_lib.prop_doc_info import Prop_Doc_Info
# Lib References
 
from .libs.service_lib.srv_classification_info import Srv_Classification_Info
from .libs.service_lib.prop_classification_info import Prop_Classification_Info

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
    obj_srv_classification_info = Srv_Classification_Info() 
    if(user_id != "" and company_id != ""):  
        lst_layouts = obj_srv_classification_info.Get_All_Classification(company_id)  
        result =  {"root_download" : settings.MEDIA_DOWNLOAD_ROOT,"result" : lst_layouts }   
             
        return render(request, 'views/classification/index.html',{'lst_classification':result})
    else:
        return render(request, 'views/login.html')
 

# Create your views here.
def add(request):

    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""): 
         
        result =  {"status" : "1", "message" : "" ,"result" : "" }        
        return render(request, 'views/classification/configuration.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')

  
