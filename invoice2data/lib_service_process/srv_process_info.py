import json
from datetime import datetime
from lib_service_db.dbconnection import DB_Connection
class Srv_Process_Info():

    def __init__(self):
        pass
    

    def get_all_fields_questions(self,company_id,config_id,field_type):
        db_query = "SELECT * FROM db_dps.tbl_configs_fields where company_id = '{}' and config_id = '{}' and field_type = '{}'"
        db_query = db_query.format(company_id,config_id,field_type)         
        objdb = DB_Connection()        
        output  = objdb.execute_query(db_query) 
        if output:
            return output
        else:
            return None



    def Insert_extracted_info(self,doc_id,page_no,extracted_json,extracted_table_json,status):
        db_query = "INSERT INTO tbl_extracted_doc(doc_id,page_no,extracted_json_location, extracted_table_json_location,status) VALUES('{}','{}','{}','{}','{}')"
        db_query = db_query.format(doc_id,page_no,extracted_json,extracted_table_json,status)          
        objdb = DB_Connection()        
        objdb.execute_non_query(db_query) 
 
    def Update_upload_doc_status(self,error_message,process_status,doc_id):    

        db_query = "UPDATE tbl_upload_doc SET  status = {} WHERE id  = '{}'"
        db_query = db_query.format(process_status,doc_id)         
        objdb = DB_Connection()        
        objdb.execute_non_query(db_query) 


    def Insert_upload_doc_history(self,error_message,process_status,doc_id):    

        db_query = "Insert into  tbl_extracted_doc_history (doc_id,status,error_message) "
        db_query = db_query + " values ({},'{}','{}')"
        db_query = db_query.format(doc_id,process_status,error_message)         
        objdb = DB_Connection()        
        objdb.execute_non_query(db_query) 

