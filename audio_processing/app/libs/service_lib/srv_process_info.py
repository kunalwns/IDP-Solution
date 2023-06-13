from app.libs.db_lib.connection import databaseconnection
import base64
from datetime import datetime 

class Srv_Process_Info:   
    def __init__(self):
        pass     

    def get_process_by_UUID(self,process_uuid):    

        db_query = "Select id from  tbl_process  WHERE process_uuid  = '{}'"
        
        db_query = db_query.format(process_uuid) 
         
        _db = databaseconnection()
        result = _db.execute_Query(db_query)  
         
        return result


    def Get_Processed_Media(self,user_id,company_id):
        db_query = "select process_doc.id ,process_doc.doc_id ,doc_name,doc_type,username, up_doc.config_id,process_start,process_end,process_status "
        db_query = db_query  + " from tbl_process process_doc "
        db_query = db_query  + " inner join tbl_upload_audio up_doc on  up_doc.id = process_doc.doc_id " 
        db_query = db_query  + " left join auth_user on  up_doc.uploaded_by = auth_user.id "                
        
        db_query = db_query  + " WHERE  up_doc.process_type != 'invoice' and auth_user.id = '{}' and process_status = 2 "
        db_query = db_query.format(user_id) 
        _db = databaseconnection()
        print(db_query)
        result = _db.execute_Query(db_query) 
        return result

    def Get_Processed_Document(self,user_id,company_id):
        db_query = "select process_doc.id,process_doc.doc_id ,doc_name,doc_type,username,config_name,up_doc.config_id,process_start,process_end,process_status "
        db_query = db_query  + " from tbl_process process_doc "
        db_query = db_query  + " inner join tbl_upload_doc up_doc on  up_doc.id = process_doc.doc_id " 
        db_query = db_query  + " inner join auth_user on  up_doc.uploaded_by = auth_user.id "                
        db_query = db_query + "  inner join tbl_configs tc on tc.id = up_doc.config_id"
        db_query = db_query  + " WHERE up_doc.process_type != 'invoice' and   auth_user.id = '{}' and process_status = 2 "
        db_query = db_query.format(user_id) 
        _db = databaseconnection()
         
        result = _db.execute_Query(db_query) 
        return result
 

    def Insert_New_Process(self,obj_process_info): 

        db_query = "INSERT INTO tbl_process "
        db_query =  db_query  + " ( process_uuid,doc_id, process_name , process_start_by  , process_status,remark,error_log,user_id,config_id,raised_datetime) "
        db_query =  db_query  + " VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
        db_query = db_query.format (obj_process_info.process_uuid,
                            obj_process_info.doc_id,
                            obj_process_info.process_name,
                            obj_process_info.process_start_by,                          
                            obj_process_info.process_status,
                            obj_process_info.remark,
                            obj_process_info.error_log,
                            obj_process_info.user_id,
                            obj_process_info.config_id,
                            obj_process_info.raised_datetime)
       
        
        _db = databaseconnection()
        _db.execute_Non_Query(db_query) 
    
    
    def Update_Process_Status_Start(self,start_date,process_status,process_uuid):    

        db_query = "UPDATE tbl_process SET  process_start = '{}' , process_status = {} WHERE process_uuid  = '{}'"
        db_query = db_query.format(start_date,process_status,process_uuid) 
        
        _db = databaseconnection()
         
        result = _db.execute_Query(db_query) 
        return result

    def Update_Process_Status_Completed(self,completed_date,process_status,process_uuid):    

        db_query = "UPDATE tbl_process SET  process_end = '{}' , process_status = {} WHERE process_uuid  = '{}'"
        db_query = db_query.format(completed_date,process_status,process_uuid) 
        
        _db = databaseconnection()
         
        result = _db.execute_Query(db_query) 
        return result

    def Update_Process_Status_Error(self,error_message,process_status,process_uuid):    

        db_query = "UPDATE tbl_process SET  error_log = '{}' , process_status = {} WHERE process_uuid  = '{}'"
        db_query = db_query.format(error_message,process_status,process_uuid) 
        
        _db = databaseconnection()
         
        result = _db.execute_Query(db_query) 
        return result        



