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
import uuid
# Lib References
from .libs.service_lib.prop_user_info import Prop_User_Info

from .libs.service_lib.prop_company_info import Prop_Company_Info
from .libs.service_lib.srv_user_info import Srv_User_Info


def create_user_Images_folders(company_id):

    # Create company Folder
    root_company = os.path.join(settings.USER_IMAGES,company_id)
    
    if(os.path.exists(root_company)):
        pass 
    else:
        os.mkdir(root_company) 

def create_data_folders(company_id):

    # Create company Folder
    root_company = os.path.join(settings.FILES_DIR,company_id)
    
    if(os.path.exists(root_company)):
        pass 
    else:
        os.mkdir(root_company)
    
    # Create Media Folder    

    root_company = os.path.join(settings.AUDIO_FILES_DIR,company_id)
    
    if(os.path.exists(root_company)):
        pass 
    else:
        os.mkdir(root_company)

    print("Data Folder Created")

@api_view(["POST"])  
def login_user(request):
    
    # read file attributes
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])            
    user_email =  dictData["user_email_id"]
    user_password = dictData["user_password"] 
    
    try:   
        obj_srv_user = Srv_User_Info()
        user_detail = obj_srv_user.User_Authenticate(user_email,user_password)
        
        if len(user_detail) > 0 :
            request.session['user_info'] = user_detail
            request.session['user_info'] = user_detail
            result =  {"status" : "1", "message" : "User Loggedin successfully", "error" : "0" } 

        else:           
            result =  {"status" : "0", "message" : "Invalid email or password", "error" : "1" } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)





@api_view(["POST"])  
def create_new_account(request):
    
     
    dictData = {}  
    dictData = ast.literal_eval(request.data["info"])    

    obj_user_info = Prop_User_Info()
    obj_company_info =  Prop_Company_Info()

    

    obj_user_info = Set_User_Info(dictData)
    obj_company_info = Set_Company_Info(dictData)
    try:

        
        obj_srv_user = Srv_User_Info()
        is_exist = obj_srv_user.Is_User_Exist(dictData["user_email_id"])        
         
        if(is_exist):            
            result =  {"status" : "0", "message" : "User Already Exists", "error" : "1" } 
        else:
            company_id = obj_srv_user.Create_New_User(obj_user_info,obj_company_info)
 

            create_data_folders(company_id)
            create_user_Images_folders(company_id)

            result =  {"status" : "1", "message" : "User Created Successfully.", "error" : "0" } 
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))  
        result =  {"status" : "0", "message" : str(e), "error" : "1" } 
        return JsonResponse(result,safe=False)
 

# Save Process Information
def Set_User_Info(dictData):
 
    obj_User_Info = Prop_User_Info()
    now = datetime.now()

    obj_User_Info.password = dictData["user_password"]
    obj_User_Info.last_login = ""
    obj_User_Info.is_superuser = "1"
    obj_User_Info.username = dictData["user_name"]
    obj_User_Info.first_name = dictData["user_name"]
    obj_User_Info.last_name = dictData["user_name"]
    obj_User_Info.email = dictData["user_email_id"] 
    obj_User_Info.is_staff = "0"
    obj_User_Info.is_active = "1"
    obj_User_Info.date_joined = str(now.strftime("%Y-%m-%d %H:%M:%S")) 
    obj_User_Info.user_id = ""
    obj_User_Info.user_uuid = str(uuid.uuid1())
    obj_User_Info.company_id = ""
    obj_User_Info.profile_photo = "user_blank.png"
    obj_User_Info.contact_number = dictData["user_contact"]

    return obj_User_Info

def Set_Company_Info(dictData):
 
    obj_company_info =  Prop_Company_Info()
    now = datetime.now()
    
    obj_company_info.company_uuid=  str(uuid.uuid1())
    obj_company_info.company_name= dictData["company_name"]
    obj_company_info.display_name= dictData["company_name"]
    obj_company_info.status= '1'
    obj_company_info.created_date = str(now.strftime("%Y-%m-%d %H:%M:%S")) 

    return obj_company_info