from app.libs.db_lib.connection import databaseconnection
import base64
import os
import pandas

class Srv_Doc_Info:   
    def __init__(self):
        pass     

    def Insert_New_Media(self,obj_doc_info):

        print(obj_doc_info)
        
        db_query = "INSERT INTO tbl_upload_audio "
        db_query =  db_query  + " ( doc_uuid, doc_name, doc_type , config_id ,uploaded_by , uploaded_date , status ) "
        db_query =  db_query  + " VALUES ('{}','{}','{}','{}','{}','{}','{}')"
        db_query = db_query.format (obj_doc_info.doc_uuid,
                            obj_doc_info.doc_name,
                            obj_doc_info.doc_type,
                            obj_doc_info.config_id,
                            obj_doc_info.uploaded_by,
                            obj_doc_info.uploaded_date,
                            obj_doc_info.status)
       
        
        _db = databaseconnection()
        _db.execute_Non_Query(db_query) 

    def Insert_New_Doc(self,obj_doc_info):
        print(obj_doc_info)
        
        db_query = "INSERT INTO tbl_upload_doc "
        db_query =  db_query  + " ( doc_uuid, doc_name, doc_type , config_id ,uploaded_by , uploaded_date , status,company_id, process_type ) "
        db_query =  db_query  + " VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')"
        db_query = db_query.format (obj_doc_info.doc_uuid,
                            obj_doc_info.doc_name,
                            obj_doc_info.doc_type,
                            obj_doc_info.config_id,
                            obj_doc_info.uploaded_by,
                            obj_doc_info.uploaded_date,
                            obj_doc_info.status,obj_doc_info.company_id, obj_doc_info.process_type)
       
        
        _db = databaseconnection()
        _db.execute_Non_Query(db_query) 
    
    
    def List_docs(self,user_id,company_id): 
        db_query = "select doc_name,doc_type,up_doc.id,username,config_name,display_name,up_doc.config_id,up_doc.uploaded_date,up_doc.status from tbl_upload_doc up_doc "
        db_query = db_query  + " inner join auth_user on  up_doc.uploaded_by = auth_user.id "                
        db_query = db_query + "  inner join tbl_configs tc on tc.id = up_doc.config_id"
        db_query = db_query  + " WHERE  up_doc.process_type = 'invoice' and  auth_user.id = '{}' order by up_doc.id desc"
        db_query = db_query.format(user_id) 
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query) 
        return result

    def List_Ready_To_Process_Docs(self,user_id,company_id): 
        db_query = "select doc_name,doc_type,up_doc.id,username,config_name,display_name,up_doc.config_id,up_doc.uploaded_date,up_doc.status from tbl_upload_doc up_doc "
        db_query = db_query  + " inner join auth_user on  up_doc.uploaded_by = auth_user.id "                
        db_query = db_query + "  inner join tbl_configs tc on tc.id = up_doc.config_id"
        db_query = db_query  + " WHERE up_doc.process_type = 'invoice' and auth_user.id = '{}' and up_doc.status in (0,1)"
        db_query = db_query.format(user_id) 
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query) 
        return result

    def List_media_documents(self,user_id,company_id):    

        db_query = "select doc_name,doc_type,up_doc.id,username,up_doc.config_id,up_doc.uploaded_date,up_doc.status from tbl_upload_audio up_doc "
        db_query = db_query  + " inner join auth_user on  up_doc.uploaded_by = auth_user.id "               
        
        db_query = db_query  + " WHERE  auth_user.id = '{}' and up_doc.status in (0,1)"
        db_query = db_query.format(user_id) 
        _db = databaseconnection()
        print(db_query)
        result = _db.execute_Query(db_query) 
        return result       

    def List_Processed_Media(self,user_id,company_id):    

        db_query = "select doc_name,doc_type,up_doc.id,username,up_doc.config_id,up_doc.uploaded_date,up_doc.status from tbl_upload_audio up_doc "
        db_query = db_query  + " inner join auth_user on  up_doc.uploaded_by = auth_user.id "              
        
        db_query = db_query  + " WHERE  auth_user.id = '{}' and up_doc.status in (1)"
        db_query = db_query.format(user_id) 
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query) 
        return result
    

    def get_nlp_detail(self,speaker,root_path,company_id,config_id,file_id,optiontype,is_sentiment):
         
        print(optiontype) 
        if optiontype == "question":            
            return self.get_question(speaker,root_path,company_id,config_id,file_id)
        if optiontype.lower() == "sentence":
            return self.get_sentence(speaker,root_path,company_id,config_id,file_id)
        if optiontype.lower() == "clarity": 
            return self.get_clarity(speaker,root_path,company_id,config_id,file_id)
        
        if is_sentiment == "1":
            # Get Sentiments
        
            return self.get_sentiments(speaker,root_path,company_id,config_id,file_id,optiontype.lower())


    def get_sentiments(self,speaker,root_path,company_id,config_id,file_id,optiontype):
        question = []
        root_dir = os.path.join(root_path,file_id,"detect_types",speaker+".csv")
         
        data = pandas.read_csv(root_dir)
        data['sentiment'] = data['sentiment'].str.lower()        
        df_quest_ans = data.loc[data['sentiment'] == optiontype] 
        
        return df_quest_ans["review"].values.tolist()


    def get_sentence(self,speaker,root_path,company_id,config_id,file_id):
        question = []
        root_dir = os.path.join(root_path,file_id,"detect_types",speaker+".csv")
         
        data = pandas.read_csv(root_dir)
        data['typeof'] = data['typeof'].str.lower()
        
        df_quest_ans = data.loc[data['typeof'] == "sentence"] 
        
        
        return df_quest_ans["review"].values.tolist()

    def get_clarity(self,speaker,root_path,company_id,config_id,file_id):
        question = []
        root_dir = os.path.join(root_path,file_id,"detect_types",speaker+".csv")
         
        data = pandas.read_csv(root_dir)
        data['typeof'] = data['typeof'].str.lower()
        
        df_quest_ans = data.loc[data['typeof'] == "clarity"] 
        
        
        return df_quest_ans["review"].values.tolist()
    
    def delete_uploaded_doc(self,doc_id):
        db_query = "Delete from tbl_upload_doc where id = {} " 
        db_query = db_query.format (doc_id)
        _db = databaseconnection()
        _db.execute_Non_Query(db_query) 
        
    def get_question(self,speaker,root_path,company_id,config_id,file_id):
        question = []
        root_dir = os.path.join(root_path,file_id,"detect_types",speaker+".csv")
         
        data = pandas.read_csv(root_dir)
        data['typeof'] = data['typeof'].str.lower()
        df_quest_ans = data.loc[data['typeof'] == "question"] 
         
        return df_quest_ans["review"].values.tolist()


# Dashboard stats

    def get_document_counts(self,company_id): 
        db_query = " select   status, count(status) as rec_count from tbl_upload_doc where company_id = '{}' group by status  " 
        db_query = db_query.format(company_id) 
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query) 
        return result


    def get_count_by_template(self,company_id):
        db_query = " SELECT config_name as name, count(tc.id)  as value  FROM db_dps.tbl_upload_doc ud inner join tbl_configs tc "
        db_query = db_query + "  on tc.id = ud.config_id where ud.company_id = '{}'  group by ud.config_id "
        
        db_query = db_query.format(company_id) 
        _db = databaseconnection()        
        result = _db.execute_Query(db_query) 
        return result
    


    def get_count_by_date(self,company_id):
        db_query = "  Select DATE_FORMAT(process_start_time, '%M %d %Y') as p_date, count(ed.id) as rec_count from tbl_extracted_doc ed "
        db_query = db_query + "  inner join tbl_upload_doc ud on ed.doc_id = ud.id  "
        db_query = db_query + "  where ud.company_id = '{}' "
        db_query = db_query + "  group by DATE_FORMAT(process_start_time, '%M %d %Y') order by DATE_FORMAT(process_start_time, '%M %d %Y') desc "         
        
        db_query = db_query.format(company_id) 
        _db = databaseconnection()        
        result = _db.execute_Query(db_query) 
        return result

    def get_count_by_doc_type(self,company_id):
        db_query = " SELECT  count(tc.id) as value, doc_type as name  FROM db_dps.tbl_upload_doc ud inner join tbl_configs tc "
        db_query = db_query + "  on tc.id = ud.config_id where ud.company_id = '{}'  group by doc_type "
        
        db_query = db_query.format(company_id) 
        _db = databaseconnection()        
        result = _db.execute_Query(db_query) 
        return result