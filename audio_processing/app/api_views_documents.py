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
from .libs.service_lib.srv_doc_info import Srv_Doc_Info
from .libs.service_lib.prop_doc_info import Prop_Doc_Info


def get_extention(filename):
    split_tup = os.path.splitext(filename)
    file_extension = split_tup[1]
    return file_extension.replace(".","")



# @api_view(["POST"])  
# def delete_document(request):
     
#     # read file attributes
#     dictData = {}  
#     dictData = ast.literal_eval(request.data["info"])   
#     company_id = get_company_id(request)
#     user_id = get_user_id(request) 
#     doc_id = dictData["doc_id"]

    
#     #Save file to the folder
#     try:  
#         obj_srv_doc_info = Srv_Doc_Info()  
#         if(user_id != "" and company_id != ""): 
#             print("deleted")
#             obj_srv_doc_info.delete_uploaded_doc(doc_id) 
#             result =  {"status" : "1", "message" : "Document has been deactivated successfully." }   
#         else:
#             result =  {"status" : "0", "message" : "User Session has expired." } 
#         return JsonResponse(result,safe=False)
#     except Exception as e:
#         result =  {"status" : "0", "message" : "Error" + str(e)  }
#         return JsonResponse(result,safe=False)   


@api_view(["POST"])  
def upload_api_check_file(request):
    
    dictData = {}  
        
    filename = request.FILES['file'].name
    fileindex = request.POST['file_index']
    config_id = request.POST['config_id']
    data = request.FILES['file']
    

    UUID =  str(uuid.uuid4().hex[:8])
        
    #Save file to the folder
    try:
        root_dir = os.path.join(settings.DOC_IMAGE_LOCATION_DIR,"dump")
        
        tmp_file = os.path.join(root_dir, filename)

        path = default_storage.save(tmp_file, ContentFile(data.read())) 
        
        result =  {"status" : "1", "message" : "File Uploaded Successfully", "file_location" : path,'fileindex' : fileindex} 
        
        return JsonResponse(result,safe=False)
    except Exception as e:
        print("Exception In Code :",str(e))     



@api_view(["POST"])  
def uploadfile(request):

    if 'user_info' in request.session:

         
        user_id = str(request.session['user_info'][0]["id"])
        company_id = str(request.session['user_info'][0]["company_id"])

        
        dictData = {}  
        
        filename = request.FILES['file'].name
        fileindex = request.POST['file_index']
        config_id = request.POST['config_id']
        data = request.FILES['file']
        

        UUID =  str(uuid.uuid4().hex[:8])
         
        #Save file to the folder
        try:
            root_dir = os.path.join(settings.FILES_DIR,company_id,config_id)
            print(root_dir)
            tmp_file = os.path.join(root_dir, filename)

            path = default_storage.save(tmp_file, ContentFile(data.read()))
            

            obj_srv_doc_info = Srv_Doc_Info()
            obj_doc_info = Prop_Doc_Info()
        
            obj_doc_info.doc_uuid = str(uuid.uuid1())
            obj_doc_info.doc_name = filename
            obj_doc_info.company_id = company_id
            obj_doc_info.doc_type = get_extention(filename)
            obj_doc_info.uploaded_by = user_id
            obj_doc_info.config_id = config_id
            obj_doc_info.uploaded_date = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            obj_doc_info.status = 0
        
        
            rec_id = obj_srv_doc_info.Insert_New_Doc(obj_doc_info) 

            result =  {"status" : "1", "message" : "File Uploaded Successfully", "file_location" : path, "record_id" : rec_id,"uuid" : UUID ,'fileindex' : fileindex} 
            
            return JsonResponse(result,safe=False)
        except Exception as e:
            print("Exception In Code :",str(e))     


