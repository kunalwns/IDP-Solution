from app.libs.db_lib.connection import databaseconnection
import base64
from datetime import datetime 

class srv_agent_docs:   
    def __init__(self):
        pass     

    def get_document_detail_by_id(self,doc_id):    

        db_query = "Select ed.*, ud.doc_name,ud.config_id from  tbl_extracted_doc ed right join tbl_upload_doc ud  " 
        db_query = db_query + " on ed.doc_id = ud.id WHERE ud.id  = '{}'"
        
        db_query = db_query.format(doc_id)          
        _db = databaseconnection()
        result = _db.execute_Query(db_query)           
        return result

    def get_document_fields(self,company_id,config_id):    

        db_query = "Select id,company_id,config_id,key_name,field_name,questions from  tbl_configs_fields " 
        db_query = db_query + " WHERE  company_id = '{}' and config_id = '{}'"
        
        db_query = db_query.format(company_id,config_id)          
        _db = databaseconnection()
        result = _db.execute_Query(db_query)           
        return result

     



