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

# Lib References
from .libs.service_lib.srv_classification_info import Srv_Classification_Info
from .libs.service_lib.prop_classification_info import Prop_Classification_Info



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

def create_layout_folders(company_id,layout_id):

    # Create company Folder
    root_company = os.path.join(settings.FILES_DIR,company_id,layout_id)
    
    if(os.path.exists(root_company)):
        pass 
    else:
        os.mkdir(root_company)    
    print("Data Folder Created")



@api_view(["POST"])  
def raise_request_train_modal(request):

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["modal_info"])   
     
    #Save file to the folder
    try:  
        obj_srv_classification_info = Srv_Classification_Info()
        obj_classification_info = Prop_Classification_Info()

        company_id = get_company_id(request)
        user_id = get_user_id(request)
        
        
        if(user_id != "" and company_id != ""):
            print(dictData)
            modal_details = obj_srv_classification_info.Insert_New_Modal_train_request(dictData,company_id) 
            dictData["train_id"] =  str(modal_details)
            try:
                response = requests.post(url = settings.CLASSIFY_API_LINK, data = dictData, timeout=2.50)  
                result =  {"status" : "1", "message" : "Request Raised successfully","error" : "0" } 
            except Exception as e:
                result =  {"status" : "0", "message" : str(e), "error" : "1" } 

              
        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print(str(e))
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)  




@api_view(["POST"])  
def get_trained_model_list(request):

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])   
    
     
    
    #Save file to the folder
    try:  
        obj_srv_classification_info = Srv_Classification_Info()
        obj_classification_info = Prop_Classification_Info()

        company_id = get_company_id(request)
        user_id = get_user_id(request)
        
        if(user_id != "" and company_id != ""):
            modal_details = obj_srv_classification_info.Get_Train_Modal_Details(dictData["id"],company_id)
            result =  {"status" : "1", "message" : "" ,"result" : modal_details }   
              
        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)  






@api_view(["POST"])  
def add_new_classifier(request):

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])   
    
     
    
    #Save file to the folder
    try:  
        obj_srv_classification_info = Srv_Classification_Info()
        obj_classification_info = Prop_Classification_Info()

        company_id = get_company_id(request)
        user_id = get_user_id(request)
         
         
        if(user_id != "" and company_id != ""):
            obj_classification_info.classification_uuid = str(uuid.uuid1())
            obj_classification_info.title =  dictData["title"]
            obj_classification_info.title = dictData["title"]
            obj_classification_info.user_id = user_id
            obj_classification_info.company_id = company_id
            obj_classification_info.status = 1
            obj_classification_info.category_list =  dictData["category_names"]
            obj_classification_info.folder_location = dictData["folder_location"]
            obj_classification_info.created_date = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')) 

            layout_exist = obj_srv_classification_info.is_config_exist(obj_classification_info.title,company_id)
            
             
            print(layout_exist)
            if layout_exist:
                result =  {"status" : "0", "message" : "Configuration " + obj_classification_info.title + " already exists." } 
            else:
                layout_id = obj_srv_classification_info.Add_new_classifier(obj_classification_info,dictData,company_id)
                
           
                result =  {"status" : "1", "message" : "Configuration has been added successfully." } 
        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)   


 

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])   
    

    
    #Save file to the folder
    try:  
        obj_srv_config_info = Srv_Config_Info()
        

        company_id = get_company_id(request)
        user_id = get_user_id(request)
        layout_id = dictData["layout_id"]
        if(user_id != "" and company_id != ""): 

            layout_details = obj_srv_config_info.Get_Layout_ByID(company_id,layout_id)
            layout_fields_detail = obj_srv_config_info.Get_Fields_By_Layout_Id(company_id,layout_id)            
            result =  {"status" : "1", "layout_details" : layout_details, "layout_fields_detail" : layout_fields_detail } 

        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)   