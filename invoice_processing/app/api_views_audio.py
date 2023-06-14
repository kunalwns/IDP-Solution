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

def Create_User_Folders(company_id,user_id):

    # Create company Folder
    root_user = os.path.join(settings.FILES_DIR,company_id,user_id)
    
    if(os.path.exists(root_user)):
        pass 
    else:
        os.mkdir(root_user)
 




@api_view(["POST"])  
def uploadfile(request):

    if 'user_info' in request.session:
         
        user_id =  get_user_id(request)
        company_id =  get_company_id(request)

        
        dictData = {}  
        
        filename = request.FILES['file'].name
        fileindex = request.POST['file_index']
        config_id = request.POST['config_id']
        data = request.FILES['file']
        

        UUID =  str(uuid.uuid4().hex[:8])
         
        #Save file to the folder
        try:
            
            
            #root_dir = os.path.join(settings.AUDIO_FILES_DIR,company_id,user_id)
            root_dir = os.path.join(settings.AUDIO_FILES_DIR)
            
            tmp_file = os.path.join(root_dir, filename)

            path = default_storage.save(tmp_file, ContentFile(data.read()))
            

            obj_srv_doc_info = Srv_Doc_Info()
            obj_doc_info = Prop_Doc_Info()
        
            obj_doc_info.doc_uuid = str(uuid.uuid1())
            obj_doc_info.doc_name = filename
            obj_doc_info.doc_type = get_extention(filename)
            obj_doc_info.uploaded_by = user_id
            obj_doc_info.config_id = config_id
            obj_doc_info.uploaded_date = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            obj_doc_info.status = 1
        
        
            rec_id = obj_srv_doc_info.Insert_New_Doc(obj_doc_info) 

            result =  {"status" : "1", "message" : "File Uploaded Successfully", "file_location" : path, "record_id" : rec_id,"uuid" : UUID ,'fileindex' : fileindex} 
            
            return JsonResponse(result,safe=False)
        except Exception as e:
            print("Exception In Code :",str(e))     


@api_view(["POST"])  
def upload_audio_file(request):

    if 'user_info' in request.session:
         
        user_id = get_user_id(request)
        company_id = get_company_id(request)

        
        dictData = {}  
        
        filename = request.FILES['file'].name
        fileindex = request.POST['file_index']
        config_id = company_id
        data = request.FILES['file']
        

        UUID =  str(uuid.uuid4().hex[:8])
         
        #Save file to the folder
        try:
            #Create_User_Folders(company_id,user_id)
            #root_dir = os.path.join(settings.AUDIO_FILES_DIR,company_id,user_id)
            root_dir = os.path.join(settings.AUDIO_FILES_DIR)
            print(root_dir)
            tmp_file = os.path.join(root_dir, filename)

            path = default_storage.save(tmp_file, ContentFile(data.read()))
            

            obj_srv_doc_info = Srv_Doc_Info()
            obj_doc_info = Prop_Doc_Info()
        
            obj_doc_info.doc_uuid = str(uuid.uuid1())
            obj_doc_info.doc_name = filename
            obj_doc_info.doc_type = get_extention(filename)
            obj_doc_info.uploaded_by = user_id
            obj_doc_info.config_id = config_id
            obj_doc_info.uploaded_date = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            obj_doc_info.status = 0
        
        
            rec_id = obj_srv_doc_info.Insert_New_Media(obj_doc_info) 

            result =  {"status" : "1", "message" : "File Uploaded Successfully", "file_location" : path, "record_id" : rec_id,"uuid" : UUID ,'fileindex' : fileindex} 
            
            return JsonResponse(result,safe=False)
        except Exception as e:
            print("Exception In Code :",str(e))     


@api_view(["POST"])  
def get_nlp_detail(request):


    if 'user_info' in request.session: 
        user_id = get_user_id(request)
        company_id = get_company_id(request)
 
        dictData = {}  
        dictData = ast.literal_eval(request.data["info"])            
        speaker =  dictData["speaker_id"]
        item_type = dictData["type"] 
        file_id = dictData["file_id"] 

        print(item_type)
        obj_doc = Srv_Doc_Info()
        #Save file to the folder
        try:
            
            if item_type.lower() == "question":
                lst_result = obj_doc.get_nlp_detail(speaker,settings.AUDIO_FILES_DIR_OUT_PUT,company_id,user_id,file_id,"question","0")
                 
                result =  {"status" : "1", "message" : "", "results" : lst_result} 
            if item_type.lower() == "sentence": 
                lst_result = obj_doc.get_nlp_detail(speaker,settings.AUDIO_FILES_DIR_OUT_PUT,company_id,user_id,file_id,"sentence","0")
                result =  {"status" : "1", "message" : "", "results" : lst_result} 

            if item_type.lower() == "clarity":
                lst_result = obj_doc.get_nlp_detail(speaker,settings.AUDIO_FILES_DIR_OUT_PUT,company_id,user_id,file_id,"Clarity","0")
                result =  {"status" : "1", "message" : "", "results" : lst_result} 


            if item_type.lower() == "positive":
                lst_result = obj_doc.get_nlp_detail(speaker,settings.AUDIO_FILES_DIR,company_id,user_id,file_id,"positive","1")
                result =  {"status" : "1", "message" : "", "results" : lst_result} 

            if item_type.lower() == "negative":
                lst_result = obj_doc.get_nlp_detail(speaker,settings.AUDIO_FILES_DIR,company_id,user_id,file_id,"negative","1")
                result =  {"status" : "1", "message" : "", "results" : lst_result} 

            if item_type.lower() == "nutral":
                lst_result = obj_doc.get_nlp_detail(speaker,settings.AUDIO_FILES_DIR,company_id,user_id,file_id,"nutral","1")
                result =  {"status" : "1", "message" : "", "results" : lst_result} 

            print(result)
            return JsonResponse(result,safe=False)
        except Exception as e:
            print("Exception In Code :",str(e))     



