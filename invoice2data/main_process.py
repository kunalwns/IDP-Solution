import flask
from flask import Flask, request, jsonify, make_response, abort
from flask_cors import CORS, cross_origin
from werkzeug import serving
from extract_data import *
import os
import datetime
from pprint import pprint
from datetime import timedelta, datetime
from lib_service_process.srv_process_info import *

from config import *
import json
from datetime import datetime
app = Flask(__name__)


@app.route('/', methods=['GET'])  
def check_exacto():
    print("hello")
    print(SENTENCE_FILE_INPUT_ROOT)
    return jsonify({"status" : "Exacto working"})

@app.route('/app/doc_process', methods=['GET', 'POST'])  
# 1. new 2. in-progress 3.completed 4. error
def doc_process():    
    #print("request.args : ",request.form)
    
    file_name =   request.form.get("document_name")
    user_id =  request.form.get("user_id")
    config_id =  request.form.get("config_id")
    doc_id =  request.form.get("document_id")     
    process_uuid =  request.form.get("process_uuid")  
    organization_id = request.form.get("organization_id")
    process_type = request.form.get("process_type")

    # file_name =  "Semester-22-23.pdf" #request.form.get("document_name")
    # user_id =  "1" #request.form.get("user_id")
    # config_id = "3" #request.form.get("config_id")
    # doc_id = "3" #request.form.get("document_id")     
    # process_uuid = "08d4b5ca-e136-11ed-95ef-0fc0afda6075" #request.form.get("process_uuid")  
    # organization_id =  "3" #request.form.get("organization_id")

      

    without_ext = os.path.splitext(file_name)[0].replace(" ", "_")

    if(process_type == "invoice"): 
        source_loaction_dir = os.path.join("/home/tarun-dev/Public/web_solution/invoice_processing/app/static/media/document/",organization_id,config_id)
        doc_folder =os.path.join("/home/tarun-dev/Public/web_solution/invoice_processing/app/static/media/document/",organization_id,config_id,"processed",doc_id)
        json_folder = os.path.join("/home/tarun-dev/Public/web_solution/invoice_processing/app/static/media/document/",organization_id,config_id,"processed",doc_id,"json")
        split_images =os.path.join("/home/tarun-dev/Public/web_solution/invoice_processing/app/static/media/document/",organization_id,config_id,"processed",doc_id,"images")
        output_dir = os.path.join("/home/tarun-dev/Public/web_solution/invoice2data/app_data/output/",organization_id,config_id,"images",without_ext)
        output_txt_dir = os.path.join("/home/tarun-dev/Public/web_solution/invoice2data/app_data/output/",organization_id,config_id,"struct_txt",without_ext)
    else:
        source_loaction_dir = os.path.join("/home/tarun-dev/Public/web_solution/audio_processing/app/static/media/document/",organization_id,config_id)
        doc_folder =os.path.join("/home/tarun-dev/Public/web_solution/audio_processing/app/static/media/document/",organization_id,config_id,"processed",doc_id)
        json_folder = os.path.join("/home/tarun-dev/Public/web_solution/audio_processing/app/static/media/document/",organization_id,config_id,"processed",doc_id,"json")
        split_images =os.path.join("/home/tarun-dev/Public/web_solution/audio_processing/app/static/media/document/",organization_id,config_id,"processed",doc_id,"images")
        output_dir = os.path.join("/home/tarun-dev/Public/web_solution/invoice2data/app_data/output/",organization_id,config_id,"images",without_ext)
        output_txt_dir = os.path.join("/home/tarun-dev/Public/web_solution/invoice2data/app_data/output/",organization_id,config_id,"struct_txt",without_ext)


    #create_init_folders(doc_folder,split_images,json_folder,output_dir,output_txt_dir)
    create_init_folders(doc_folder,source_loaction_dir,json_folder,output_dir,output_txt_dir)
    objsrv = Srv_Process_Info()
    # Process START
    start_date_time = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    # set doc as in progress state
    objsrv.Update_upload_doc_status("","2",doc_id)

    try: 

        print("Processing...")

        #pre_process_doc(file_name,source_loaction_dir,split_images)
        field_data = {}
        tabular_data = {}
        results = process_start_extraction(file_name,source_loaction_dir,output_dir,output_txt_dir,organization_id,config_id,doc_id,json_folder,process_type)         
        # # Insert Extracted Output into db table
        # objsrv.Insert_extracted_info(doc_id,loc_json_data,loc_json_data,"3")
         
        # Upate doc status completed
        objsrv.Update_upload_doc_status("","3",doc_id)

        return jsonify({'sucess':'true',"process_status" : "Completed"})
    except Exception as e:
        print(str(e))       
        # Updating Process has Error in extraction
        objsrv.Update_upload_doc_status("Error in running process to extract","4",doc_id)
        objsrv.Insert_upload_doc_history(str(e),"4",doc_id)
        return jsonify({'sucess':'false',"process_status" : "Error and imcompleted"})

     



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug = True)