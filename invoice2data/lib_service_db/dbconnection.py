import json

import pprint, traceback

import os

from collections import OrderedDict

import mysql.connector

# DATABASE_NAME = os.environ.get('DB_NAME','db_exacto')
# DATABASE_USER = os.environ.get('DB_USER','SA')
# DATABASE_PASSWORD = os.environ.get('DB_PASSWORD','Exacto_Prod')
# DATABASE_HOST = os.environ.get('DB_HOST','127.0.0.1')
# DATABASE_PORT = os.environ.get('DB_PORT','1433')



class DB_Connection():

    DATABASE_NAME = "db_dps"
    DATABASE_USER = "root"
    DATABASE_PASSWORD = "T@rungoy@l1234"
    DATABASE_HOST = "localhost"
    DATABASE_PORT = "3306"
    

    def __init__(self):

         self.mydb = mysql.connector.connect(host = 'localhost',port= 3306, database='db_dps',user='root',password='T@rungoy@l1234',auth_plugin='mysql_native_password')

      
   
    def execute_non_query(self,query):
        try:
            mycursor = self.mydb.cursor()
            mycursor.execute(query)
            self.mydb.commit()
            return 'success'
        except:
            print("Error in db")
            traceback.print_exc()


    def execute_query(self,query):
        myresult = []
        #mydb = connect_db()
        mycursor = self.mydb.cursor()

        mycursor.execute(query)

        myresult = self.dictfetchall(mycursor)

        return myresult


     
    def dictfetchall(self,cursor):
         
        columns = [col[0]

        for col in cursor.description]
        return [OrderedDict(zip(columns, row))
        for row in cursor.fetchall()

        ]






