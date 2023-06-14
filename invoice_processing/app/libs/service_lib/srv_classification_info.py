from app.libs.db_lib.connection import databaseconnection
import base64


class Srv_Classification_Info:   
    
    def __init__(self):
        pass     


    def Get_All_Classification(self,company_id):
        db_query = "select * from tbl_classification_layouts where company_id = '{}'"         
        db_query = db_query.format(company_id)  
        _db = databaseconnection()        
        result = _db.execute_Query(db_query)
        return result

    def Get_All_Modal(self,company_id):
        db_query = "select * from tbl_classification_training where company_id = '{}'"         
        db_query = db_query.format(company_id)  
        _db = databaseconnection()        
        result = _db.execute_Query(db_query)
        return result

    def Get_Train_Modal_Details(self,id,company_id):
        db_query = "select * from tbl_classification_training where  classifier_id = '{}'"         
        db_query = db_query.format(id)  
        _db = databaseconnection()        
        result = _db.execute_Query(db_query)
        return result

 

    def Get_Layout_ByID(self,company_id,layout_id):
        db_query = "select  * from tbl_configs where company_id = '{}' and id  = '{}' "         
        db_query = db_query.format(company_id,layout_id) 
        print(db_query)
        _db = databaseconnection()        
        result = _db.execute_Query(db_query)
        return result
 

    def is_config_exist(self,config_name,company_id):
        db_query = "select count(id) as reccount from tbl_classification_layouts where title = '{}' and company_id = '{}' "         
        db_query = db_query.format(config_name,company_id) 
         
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query)
        
        if(result[0]['reccount'] == 1):
            return True
        else:
            return False

    def Add_new_classifier(self,obj_config_info,dict_fields,company_id):
        try:
            # Insert Into COnfig master
            last_inserted_id = self.Insert_New_Classifier_Info(obj_config_info) 
            return str(last_inserted_id)
        except Exception as e:
            raise Exception(str(e)) 


    def Insert_New_Modal_train_request(self,obj_config_info,company_id): 
        db_query = "INSERT INTO tbl_classification_training   "
        db_query =  db_query  + " (classifier_id, train_status,company_id,modal_name) "
        db_query =  db_query  + " VALUES ('{}','{}','{}','{}')"
        db_query = db_query.format (obj_config_info["classifier_id"],
                            "1",                           
                            company_id,
                            obj_config_info["modal_name"])
       
        print(db_query)
        _db = databaseconnection()
        last_inserted_id = _db.execute_Query_return_last_inserted(db_query) 
        return last_inserted_id
    

    def Insert_New_Classifier_Info(self,obj_config_info): 
        db_query = "INSERT INTO tbl_classification_layouts   "
        db_query =  db_query  + " ( user_id, company_id, classification_uuid , title ,description , created_date, category_list,status,folder_location) "
        db_query =  db_query  + " VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')"
        db_query = db_query.format (obj_config_info.user_id,
                            obj_config_info.company_id,                           
                            obj_config_info.classification_uuid,
                            obj_config_info.title,
                            obj_config_info.description,
                            obj_config_info.created_date,
                            obj_config_info.category_list,
                            obj_config_info.status,
                            obj_config_info.folder_location)
       
        
        _db = databaseconnection()
        last_inserted_id = _db.execute_Query_return_last_inserted(db_query) 
        return last_inserted_id
    
  