from django.shortcuts import render

from .libs.service_lib.srv_doc_info import Srv_Doc_Info
from .libs.service_lib.prop_doc_info import Prop_Doc_Info
# Lib References
from .libs.service_lib.srv_process_info import Srv_Process_Info
from .libs.service_lib.srv_config_info import Srv_Config_Info
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

    if(user_id != "" and company_id != ""):  
        obj_srv_doc_info = Srv_Doc_Info()
        results = obj_srv_doc_info.List_media_documents(user_id,company_id)
         
        result =  {"status" : "1", "message" : "" ,"result" : results }        
        return render(request, 'views/audio/index.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')


def media_files(request):
    company_id = get_company_id(request)
    user_id = get_user_id(request)

    if(user_id != "" and company_id != ""):  
        obj_srv_doc_info = Srv_Doc_Info()
        results = obj_srv_doc_info.List_media_documents(user_id,company_id)
        print(results)
        result =  {"status" : "1", "message" : "" ,"result" : results }        
        return render(request, 'views/audio/uploaded_files.html',{'doc_list':result})
    else:
        return render(request, 'views/login.html')


def upload(request):

    obj_srv_config_info = Srv_Config_Info() 

    company_id = get_company_id(request)
    user_id = get_user_id(request)
        
    if(user_id != "" and company_id != ""):         
        lst_layouts = obj_srv_config_info.Get_All_Configs(company_id)  
        return render(request, 'views/audio/upload.html',{'lst_layouts':lst_layouts})
    else:
        return render(request, 'views/login.html')

def processed(request):
    company_id = get_company_id(request)
    user_id = get_user_id(request)
    obj_srv_processed_doc  = Srv_Process_Info()
    results = obj_srv_processed_doc.Get_Processed_Media(user_id,company_id)
    print(results)
    result =  {"status" : "1", "message" : "" ,"result" : results }
    return render(request, 'views/audio/processed.html',{'doc_list':result})


def analysis(request,id):
    media_analysis = {}
    company_id = get_company_id(request)
    user_id = get_user_id(request)
    obj_srv_processed_doc  = Srv_Process_Info()
    
    nlp_stats = read_nlp_stats(company_id,user_id,"6313")

    # Set analysis for overall Stats
    media_analysis["stats"] = nlp_stats


    speakers_count = nlp_stats["speaksers"]
    speakers_name = nlp_stats["speaksers_name"]
    # READ DATA
    results = read_csv(nlp_stats,speakers_count,speakers_name,company_id,user_id,"6313")
    overall_details = read_all_speakers(nlp_stats,speakers_count,speakers_name,company_id,user_id,"6313")
    # Set analysis for Speakers

    media_analysis["overall_details"] = overall_details    
     
    media_analysis["speakers_stats"] = results

    result =  {"status" : "1", "message" : "" ,"result" : media_analysis }
    return render(request, 'views/audio/analysis.html',{'dashboard_stats':result,'rec_id':str(id)})


 

def read_nlp_stats(company_id,config_id,file_id):
    nlp_stats = {}
    root_dir = os.path.join(settings.AUDIO_FILES_DIR,company_id,config_id,"outputs",file_id,"nlp_stats.json") 
    all_txt_url = os.path.join(company_id,config_id,"outputs",file_id,"speakers_audio_text","all.txt") 
    f = open (root_dir, "r")
    try: 
        nlp_stats = json.loads(f.read()) 
        nlp_stats["all_url"] = all_txt_url
    except e:
        nlp_stats = None
        pass
    finally:
        f.close
    return nlp_stats
  


def read_all_speakers(nlp_stats,speakers_count,speakers_name,company_id,config_id,file_id):

    stats = {}
    root_dir = os.path.join(settings.AUDIO_FILES_DIR,company_id,config_id,"outputs",file_id,"speaker_nlp","overall.csv")
    data = pandas.read_csv(root_dir) 
    
    df_quest_ans = data.groupby(['type'])['type'].count().reset_index(name='counts')

     
    df_sentiments = data.groupby(['sentiment'])['sentiment'].count().reset_index(name='counts')

    df_overall_sentiments = data.groupby(['sentiment'])['sentiment'].max().reset_index(name='counts').sort_values(['counts'], ascending=True)
    
    

    #data.query('type == "Question"', inplace = True)
    for name in df_quest_ans.index:
        print(df_quest_ans.loc[name].type)        
        stats[df_quest_ans.loc[name].type] = df_quest_ans.loc[name].counts 
         

    for name in df_sentiments.index:
        #print(name)
        stats[df_sentiments.loc[name].sentiment] = df_sentiments.loc[name].counts
    
    for name in df_overall_sentiments.index:
        #print(name)
        stats["audio_sentiment"] = df_overall_sentiments.loc[name].counts
        break
    return stats

 

def read_csv(nlp_stats,speakers_count,speakers_name,company_id,config_id,file_id): 
    lst_speakers = []  

    speakers_time_spent = nlp_stats["speaksers_time_spent"]
     
    
    for spker in speakers_name:
        stats = {}
        root_dir = os.path.join(settings.AUDIO_FILES_DIR,company_id,config_id,"outputs",file_id,"speaker_nlp",spker+".csv")
        txt_path = os.path.join(company_id,config_id,"outputs",file_id,"speakers_audio_text",spker+".txt")
        data = pandas.read_csv(root_dir)
        stats["url"] = txt_path
        stats["speaker"] = spker
        stats["speaker_display"] = spker.replace("_"," - ")
        stats["time_spent"] = speakers_time_spent[0][spker]
        df_quest_ans = data.groupby(['type'])['type'].count().reset_index(name='counts')
        df_sentiments = data.groupby(['sentiment'])['sentiment'].count().reset_index(name='counts')
        #data.query('type == "Question"', inplace = True)
        for name in df_quest_ans.index:
            #print(name)
            stats[df_quest_ans.loc[name].type] = df_quest_ans.loc[name].counts 

        for name in df_sentiments.index:
            #print(name)
            stats[df_sentiments.loc[name].sentiment] = df_sentiments.loc[name].counts 

        lst_speakers.append(stats)
    
    return lst_speakers
