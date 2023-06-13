import json
from datetime import datetime
from lib_service_db.dbconnection import DB_Connection

class Srv_Classifier_Info():

    def __init__(self):
        pass
    
    def Insert_trained_model(self,dict_items): 
        db_query = " INSERT INTO tbl_classification_training (classifier_id,modal_name,trained_model_path,train_start,train_end,train_status,company_id) " 
        db_query = db_query  + " VALUES ('" + str(dict_items["classifier_id"]) + "',"
        db_query = db_query  + "'" + dict_items["modal_name"] + "',"
        db_query = db_query  + "'" + dict_items["trained_model_path"] + "',"
        db_query = db_query  + "'" + dict_items["train_start"] + "',"
        db_query = db_query  + "'" + dict_items["train_end"] + "',"
        db_query = db_query  + "'" + dict_items["train_status"] + "',"
        db_query = db_query  + "'" + str(dict_items["company_id"]) + "')"

        objdb = DB_Connection()
        
        output  = objdb.execute_non_query(db_query) 
        if output:
            return ""
        else:
            return None
          

    def get_classifer_config_by_id(self,id):    

        db_query = "SELECT * FROM db_dps.tbl_classification_layouts where id  = '{}'"
        db_query = db_query.format(id) 
        
        objdb = DB_Connection()
        
        output  = objdb.execute_query(db_query) 
        if output:
            return output[0]
        else:
            return None
          