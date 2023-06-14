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
from .libs.service_lib.srv_config_info import Srv_Config_Info
from .libs.service_lib.prop_config_info import Prop_Config_Info



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
def delete_layout(request):

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])   
    company_id = get_company_id(request)
    user_id = get_user_id(request) 
    layout_id = dictData["layout_id"]

    
    #Save file to the folder
    try:  
        obj_srv_config_info = Srv_Config_Info()  
        if(user_id != "" and company_id != ""): 
            print("deleted")
            obj_srv_config_info.delete_layout(layout_id,company_id) 
            result =  {"status" : "1", "message" : "Layout has been deactivated successfully." }   
        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)   




@api_view(["POST"])  
def delete_field(request):

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])   
    company_id = get_company_id(request)
    user_id = get_user_id(request) 
    field_id = dictData["id"]

    
    #Save file to the folder
    try:  
        obj_srv_config_info = Srv_Config_Info()  
        if(user_id != "" and company_id != ""): 
            print("deleted")
            obj_srv_config_info.delete_field(field_id,company_id) 
            result =  {"status" : "1", "message" : "Field has been deleted successfully." }   
        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)   


@api_view(["POST"])  
def add_new_field(request):

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])   
    company_id = get_company_id(request)
    user_id = get_user_id(request)
    print(company_id)
    layout_id = dictData["layout_id"]

    
    #Save file to the folder
    try:  
        obj_srv_config_info = Srv_Config_Info() 
       
        if(user_id != "" and company_id != ""):
            print("inserted")
            obj_srv_config_info.Insert_New_Config_single_fields(layout_id,dictData,company_id)

            result =  {"status" : "1", "message" : "Field has been added successfully." }   
        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)   

 

@api_view(["POST"])  
def add_new_config(request):

    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])   
     
    
    #Save file to the folder
    try:  
        obj_srv_config_info = Srv_Config_Info()
        obj_config_info = Prop_Config_Info()

        company_id = get_company_id(request)
        user_id = get_user_id(request)
        
        if(user_id != "" and company_id != ""):
            obj_config_info.config_uuid = str(uuid.uuid1())
            obj_config_info.config_name =  dictData[0]["config_name"]
            obj_config_info.display_name = dictData[0]["config_name"]
            obj_config_info.user_id = user_id
            obj_config_info.company_id = company_id
            obj_config_info.status = 1
            obj_config_info.created_date = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')) 

            

            layout_exist = obj_srv_config_info.is_config_exist(obj_config_info.config_name,company_id)
            if layout_exist:
                result =  {"status" : "0", "message" : "Layout " + obj_config_info.config_name + " already exists." } 
            else:
                layout_id = obj_srv_config_info.Add_new_layout(obj_config_info,dictData,company_id)
                
                create_layout_folders(company_id,layout_id) 

                result =  {"status" : "1", "message" : "Layout has been added successfully." } 
        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)   

 

@api_view(["POST"])  
def api_layout_detail(request):

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
            print(layout_fields_detail)
            result =  {"status" : "1", "layout_details" : layout_details, "layout_fields_detail" : layout_fields_detail } 

        else:
            result =  {"status" : "0", "message" : "User Session has expired." } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        result =  {"status" : "0", "message" : "Error" + str(e)  }
        return JsonResponse(result,safe=False)   