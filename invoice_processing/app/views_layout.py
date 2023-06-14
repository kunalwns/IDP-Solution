from django.shortcuts import render

from .libs.service_lib.srv_config_info import Srv_Config_Info
from .libs.service_lib.prop_config_info import Prop_Config_Info
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

    obj_srv_config_info = Srv_Config_Info() 

    company_id = get_company_id(request)
    user_id = get_user_id(request)
        
    if(user_id != "" and company_id != ""):         
        lst_layouts = obj_srv_config_info.Get_All_Configs(company_id)  
        result =  {"status" : "1", "message" : "" ,"result" : lst_layouts }   
        return render(request, 'views/layouts/index.html',{'lst_layouts':lst_layouts})
    else:
        return render(request, 'views/login.html')


def add(request):
    return render(request, 'views/layouts/add.html')

 
