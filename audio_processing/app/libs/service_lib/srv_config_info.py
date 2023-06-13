from app.libs.db_lib.connection import databaseconnection
import base64


class Srv_Config_Info:   
    
    def __init__(self):
        pass     


    def Get_All_Configs(self,company_id):
        db_query = "select id,config_uuid, config_name, display_name,created_date,status from tbl_configs where company_id = '{}' and status = 1 "         
        db_query = db_query.format(company_id) 
         
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

    def Get_Fields_By_Layout_Id(self,company_id,layout_id):
        db_query = "select  * from tbl_configs_fields where company_id = '{}' and config_id  = '{}' "         
        db_query = db_query.format(company_id,layout_id) 
         
        _db = databaseconnection()        
        result = _db.execute_Query(db_query)
        return result

    def delete_layout(self,layout_id,company_id):
        db_query = "Update  tbl_configs set status = 0 where id = '{}' and company_id = '{}' "         
        db_query = db_query.format(layout_id,company_id) 
         
        _db = databaseconnection() 
        _db.execute_Non_Query(db_query)
        return True

    def delete_field(self,field_id,company_id):
        db_query = "Delete from tbl_configs_fields where id = '{}' and company_id = '{}' "         
        db_query = db_query.format(field_id,company_id) 
         
        _db = databaseconnection() 
        _db.execute_Non_Query(db_query)
        return True

    def is_config_exist(self,config_name,company_id):
        db_query = "select count(id) as reccount from tbl_configs where config_name = '{}' and company_id = '{}' "         
        db_query = db_query.format(config_name,company_id) 
         
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query)
        
        if(result[0]['reccount'] == 1):
            return True
        else:
            return False

    def Add_new_layout(self,obj_config_info,dict_fields,company_id):
        try:
            # Insert Into COnfig master
            last_inserted_id = self.Insert_New_Config(obj_config_info)

            # Insert Fields information
            self.Insert_New_Config_fields(last_inserted_id,dict_fields,company_id)
            return str(last_inserted_id)
        except Exception as e:
            raise Exception(str(e)) 


    def Insert_New_Config(self,obj_config_info):
        
        db_query = "INSERT INTO tbl_configs  "
        db_query =  db_query  + " ( config_uuid, config_name, display_name , user_id ,company_id , status, created_date) "
        db_query =  db_query  + " VALUES ('{}','{}','{}','{}','{}','{}','{}')"
        db_query = db_query.format (obj_config_info.config_uuid,
                            obj_config_info.config_name,                           
                            obj_config_info.display_name,
                            obj_config_info.user_id,
                            obj_config_info.company_id,
                            obj_config_info.status,
                            obj_config_info.created_date)
       
        
        _db = databaseconnection()
        last_inserted_id = _db.execute_Query_return_last_inserted(db_query) 
        return last_inserted_id
    
 


    def Insert_New_Config_fields(self,layout_id,dict_fields,company_id):
        try:
            query_statement = ""
            i = 0
            query_statement = " INSERT INTO tbl_configs_fields ( company_id,config_id,field_name,field_datatype,field_type,sub_type,questions,is_active,key_name ) "
            query_statement = query_statement + " VALUES "            
            all_inserts = ""
            i = 0
            for i  in range(len(dict_fields)-1):
                insert_statements = ""
                field =  dict_fields[i+1]["field"]
                field_data_type = dict_fields[i+1]["field_data_type"]
                field_type =  dict_fields[i+1]["field_type"]
                sub_type =  dict_fields[i+1]["sub_type"]
                field_keywords =  dict_fields[i+1]["field_keywords"]
                field_key_name = dict_fields[i+1]["key_name"]
                insert_statements =   " ('{}','{}','{}','{}','{}','{}','{}','{}','{}'),"
                insert_statements = insert_statements.format(company_id,
                            layout_id,
                            field,
                            field_data_type,
                            field_type,
                            sub_type,
                            field_keywords,
                            "1",field_key_name)                 
                all_inserts = all_inserts + insert_statements
                 
            query_statement = query_statement + all_inserts[:-1] + ";"
            print(query_statement)
            _db = databaseconnection()
            _db.execute_Non_Query(query_statement) 
         
        except Exception as e:
            raise Exception(str(e)) 

    

    def Insert_New_Config_single_fields(self,layout_id,dict_fields,company_id):
        try:
            query_statement = ""
            i = 0
            query_statement = " INSERT INTO tbl_configs_fields ( company_id,config_id,field_name,field_datatype,field_type,sub_type,questions,is_active,key_name ) "
            query_statement = query_statement + " VALUES "

            field =  dict_fields["field"]
            field_data_type = dict_fields["field_data_type"]
            field_type =  dict_fields["field_type"]
            sub_type =  dict_fields["sub_type"]
            field_keywords =  dict_fields["field_keywords"]
            field_key_name = dict_fields["key_name"]
            insert_statements =   " ('{}','{}','{}','{}','{}','{}','{}','{}','{}')"
            insert_statements = insert_statements.format(company_id,
                        layout_id,
                        field,
                        field_data_type,
                        field_type,
                        sub_type,
                        field_keywords,
                        "1",field_key_name)       
            
            query_statement = query_statement + insert_statements             
            _db = databaseconnection()
            _db.execute_Non_Query(query_statement) 
         
        except Exception as e:
            raise Exception(str(e)) 

        