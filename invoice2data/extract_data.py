
import re
import spacy
import cv2
import pytesseract
from pytesseract import Output
import pandas as pd
import os
import json
import shutil
from convert_pdf_to_image import *
from lib_service_process.srv_process_info import *
from api_call import *
from config import *

class FakeDict(dict):
    def __init__(self, items):
        self['something'] = 'something'
        self._items = items
    def items(self):
        return self._items


# Get fields detail from database
def get_fields_questions(company_id,config_id,field_type):
    lst_form_fields = []
    objsrv = Srv_Process_Info()
    lst_form_fields = objsrv.get_all_fields_questions(company_id,config_id,field_type)
    return  lst_form_fields 

# ITerate fields and questions
def parse_question_list(lst_form_fields):
    array_of_tuples = [] 
    for item in lst_form_fields:
        array_of_tuples.append(("question", dict(item)["questions"]))

    obj = json.dumps(dict(array_of_tuples))    
    json_question = FakeDict(array_of_tuples)  
    return json_question
# ITerate fields and questions
# def parse_question_list(lst_form_fields):
#     array_of_tuples = [] 
     
#     for item in lst_form_fields:
          
#         array_of_tuples.append(("question", dict(item)["questions"]))
    
#     str_items = ""
#     for i in array_of_tuples:
#         str_items =  str_items + ",{'question' : '" + i[1] + "'}"         
    
#     return str_items[1:]      
    


def dump_json_into_file(page_name, dump_location,json_object):  
    
    with open(dump_location, 'w+') as f:
        json.dump(json_object, f)


def  pre_process_doc(file_name,source_loaction_dir,split_images):
    split_tup = os.path.splitext(file_name)
    file_extension = split_tup[1]
    if(file_extension.lower() == ".pdf"):
        pdf_to_image_convert(file_name,source_loaction_dir,split_images)
    else:
        
        shutil.copy(os.path.join(source_loaction_dir,file_name), os.path.join(split_images,file_name))


def get_file_list(company_id,config_id,doc_id): 
    src_location_dir = os.path.join(DOC_IMAGE_LOCATION_DIR,company_id,config_id,"processed",doc_id,"images")
    dir_list = os.listdir(src_location_dir)
    return dir_list

# PRocess Start function
def process_start_extraction(file_name,source_loaction_dir,output_dir,output_txt_dir,company_id,config_id,doc_id,json_folder,process_type):


    file_without_ext = os.path.splitext(file_name)[0]
    

    src_file = os.path.join(source_loaction_dir,file_name)
    
    # Extract Form Data
    lst_form_fields = get_fields_questions(company_id,config_id,"Form") 
    dict_form_questions = parse_question_list(lst_form_fields) 

    #dict_pages = get_file_list(company_id,config_id,doc_id)
    objsrv = Srv_Process_Info()  
    try: 
        page_without_ext = file_without_ext
        page_name = page_without_ext 
        format_file_name = doc_id + "_" + page_name+".json"
        data_bump_location = os.path.join(json_folder,format_file_name)
        
        if(process_type == "invoice"):
            api_response_json = call_invoice_api_get_data(src_file,dict_form_questions) 
        else:
            api_response_json = call_api_get_data(src_file,dict_form_questions) 
    
        # Save JSON Response to folder
        dump_json_into_file(page_name, data_bump_location,api_response_json)
        
        # Insert Extracted Output into db table
        objsrv.Insert_extracted_info(doc_id,page_name,{},{},"3")
    except Exception as e:
        api_resp = {"data": [{"status": "not able to fetch"}]}
        dump_json_into_file(page_name, data_bump_location,api_resp)
        objsrv.Insert_extracted_info(doc_id,page_name,{},{},"4")
    return {}
 

def create_init_folders(doc_folder,split_images,json_folder,output_dir,output_txt_dir):
    # Create DOcument folder for outputs
    
    if not os.path.isdir(doc_folder):
        os.makedirs(doc_folder)    

    # Create split images folder for outputs
    if not os.path.isdir(split_images):
        os.makedirs(split_images)        

    # Create Json FOlder 
    if not os.path.isdir(json_folder):
        os.makedirs(json_folder)     

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    if not os.path.isdir(output_txt_dir):
        os.makedirs(output_txt_dir)
    
 


