from django.shortcuts import render
from .libs.service_lib.srv_doc_info import Srv_Doc_Info
import json

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
    obj_srv_doc_info = Srv_Doc_Info()
 
 
    stats = {"uploaded" : 0, "processed" : 0, "inprogress" : 0, "failed" : 0}
    if(user_id != "" and company_id != ""): 
        count_status = obj_srv_doc_info.get_document_counts(company_id) 
        lst_item = json.dumps(count_status)
        aList = json.loads(lst_item) 
        total_uploaded = 0
        for item in aList: 
            if (item["status"] == 4):
                print("hello")
                stats["failed"] = str(item["rec_count"])
                total_uploaded= total_uploaded + int(item["rec_count"])
            if(item["status"] == 3):
                stats["processed"] = str(item["rec_count"])
                total_uploaded= total_uploaded + int(item["rec_count"])
            if(item["status"] == 2):
                stats["inprogress"] = str(item["rec_count"])
                total_uploaded= total_uploaded + int(item["rec_count"])
            if(item["status"] == 1 or item["status"] == 0  ):                 
                total_uploaded= total_uploaded + int(item["rec_count"])
        stats["uploaded"] = str(total_uploaded)
        
        
        # Get Graph Data
        data_pie_template = obj_srv_doc_info.get_count_by_template(company_id)
        data_pie_doc_type = obj_srv_doc_info.get_count_by_doc_type(company_id)
        data_doc_7_days = obj_srv_doc_info.get_count_by_date(company_id)
        graph_data = {"template" : json.dumps(data_pie_template),"doc_type" : json.dumps(data_pie_doc_type)}
        result =  {"status" : "1", "message" : "" ,"result" : stats , "graph_data" : graph_data, "tbl_data" : json.dumps(data_doc_7_days) }   
        return render(request, 'views/dashboard/index.html',{'doc_stats':result})
    else:
        return render(request, 'views/login.html')


 