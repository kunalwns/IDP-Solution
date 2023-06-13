from app.libs.db_lib.connection import databaseconnection
import base64


class Srv_Extraction_Info:   
    def __init__(self):
        pass     


    def Get_standard_fields(self,process_id):
        db_query = "SELECT ts.* , config_id FROM db_dps.tbl_process tp inner join tbl_standard_fields  ts on ts.process_id = tp.id where ts.process_id = {} limit 1".format(process_id) 
        
        _db = databaseconnection()
        print(db_query)
        result = _db.execute_Query(db_query) 
        return result

    def Get_standard_lineitems_fields(self,process_id):
       
        db_query = "Select id,doc_id,process_id,line_no,order_number,unit,description,unit_price,total_amount,quantity,amount  from tbl_lineitem_standard_fields where process_id = {} ".format(process_id) 
        print(db_query)
        _db = databaseconnection()
        result = _db.execute_Query(db_query) 
        return result
    
    
    def List_docs(self,user_id,config_id):    

        db_query = "select doc_name,doc_type,up_doc.id,username,config_name,up_doc.config_id,up_doc.uploaded_date,up_doc.status from tbl_upload_doc up_doc "
        db_query = db_query  + " inner join auth_user on  up_doc.uploaded_by = auth_user.id "                
        db_query = db_query + "  inner join tbl_configs tc on tc.id = up_doc.config_id"
        db_query = db_query  + " WHERE config_id = '{}' and auth_user.id = '{}' and status in (0,1)"
        db_query = db_query.format(user_id,config_id) 
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query) 
        return result

        
        