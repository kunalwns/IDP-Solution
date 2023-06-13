from django.db import connection, transaction
from collections import OrderedDict
class databaseconnection(object):
     
    def dictfetchall(self,cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            OrderedDict(zip(columns, row))
            for row in cursor.fetchall()
        ]
     
    def __init__(self):
        #print("Instantiating!")\
        pass

    def execute_Non_Query(self, query):
        
        cursor = connection.cursor()
        cursor.execute(query)
        return 'success'

    def execute_Query(self, query):
          
        cursor = connection.cursor()
        cursor.execute(query)        
        row = self.dictfetchall(cursor)
        return row
    
    def execute_Query_return_last_inserted(self,query):
        cursor = connection.cursor()
        cursor.execute(query) 
        return cursor.lastrowid