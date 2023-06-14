from app.libs.db_lib.connection import databaseconnection
import base64


class Srv_User_Info:

    def __init__(self):
        pass     


    def User_Authenticate(self,user_email,user_password):

        db_query = "SELECT au.id,username,email,company_id,company_name,profile_photo FROM  auth_user au  inner join tbl_user_details ud on ud.user_id = au.id inner join tbl_company tc on tc.id = ud.company_id "
        db_query = db_query  + " where email = '{}' and password = '{}'"         
        db_query = db_query.format(user_email,user_password) 
        print(db_query)
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query)
        print(result)
        return result
        



    def Is_User_Exist(self,user_email):
        db_query = "select count(id) as reccount from auth_user where email = '{}'"         
        db_query = db_query.format(user_email) 
        print(db_query)
        _db = databaseconnection()
        
        result = _db.execute_Query(db_query)
        print(result[0]['reccount'])
        if(result[0]['reccount'] == 1):
            return True
        else:
            return False
         

    def Create_New_User(self,obj_User_info,obj_Company_info):
        

        user_id = self.Insert_User_Auth(obj_User_info)
        
        obj_User_info.user_id = user_id


        company_id = self.Insert_Company_Detail(obj_Company_info)
         
        self.Insert_User_Detail(obj_User_info,user_id,company_id) 
        
        return str(company_id)

    def Insert_User_Auth(self,obj_user_info):
        
        db_query = " INSERT INTO auth_user (password , is_superuser ,username , first_name , last_name ,email , is_staff , is_active , date_joined,user_uuid ) "
        db_query = db_query + "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
        db_query =  db_query.format(obj_user_info.password,                        
                        obj_user_info.is_superuser ,
                        obj_user_info.username , 
                        obj_user_info.first_name , 
                        obj_user_info.last_name ,
                        obj_user_info.email , 
                        obj_user_info.is_staff , 
                        obj_user_info.is_active , 
                        obj_user_info.date_joined,
                        obj_user_info.user_uuid)
        
        
         
        _db = databaseconnection()
        last_inserted_id = _db.execute_Query_return_last_inserted(db_query) 
        return last_inserted_id
 
    def Insert_User_Detail(self,obj_user_info,user_id,company_id): 

        db_query = " INSERT INTO tbl_user_details (user_id,user_uuid,company_id,profile_photo,contact_number) "
        db_query = db_query + "VALUES ('{}','{}','{}','{}','{}')"
        db_query =  db_query.format(user_id,
                        obj_user_info.user_uuid , 
                        company_id ,
                        obj_user_info.profile_photo , 
                        obj_user_info.contact_number 
                        )
        _db = databaseconnection()
        print(db_query)
        last_inserted_id = _db.execute_Non_Query(db_query) 
         
    def Insert_Company_Detail(self,obj_company_info):
        db_query = " INSERT INTO tbl_company (company_uuid,company_name,display_name,status,created_date) "
        db_query = db_query + "VALUES ('{}','{}','{}','{}','{}')"
        db_query =  db_query.format(obj_company_info.company_uuid,
                        obj_company_info.company_name , 
                        obj_company_info.display_name ,
                        obj_company_info.status , 
                        obj_company_info.created_date 
                        )
        _db = databaseconnection()
        print(db_query)
        last_inserted_id = _db.execute_Query_return_last_inserted(db_query) 
        return last_inserted_id