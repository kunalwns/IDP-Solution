import json
import itertools
extract_data = {
    "results": {
        "Line_Items": {
            "colums": [
                "",
                "Items  Ordered",
                "Price \n"
            ],
            "rows": [
                [
                    "",
                    "1 of: Signoraware Aqua Fresh Water Bottle, 1 Litre, Floro Green",
                    "140.00 \n"
                ]
            ]
        },
        "fields": [
            {
                "Billing_address": "Tarun Kumar a. lied: - 3rd Floor, Plot No Q 1/21 Promotion Applied 43-00 SOUTH CITY 2, Sector 49 GURGAON, HARYANA 122018 Grand Total: 97.00",
                "Delivery_address": "ARUN KUMAR 605 to 610, Bestech Business Tower, Sector 48 Sohna Road GURGAON, HARYANA 122018 India",
                "Invoice_date": "19 December   2016",
                "Total Amount": "97.00",
                "company_name": "Amazon.com, Inc.",
                "invoice_number": "407-4081070-4193960"
            }
        ]
    },
    "sucess": "1"
}




def parse_standard_fields(extract_data,doc_id,process_id):

    print(extract_data)

    created_date = "2022-10-10 0:20 PM"
    dct = extract_data["results"]["fields"]

    print(dct[0]["Billing_address"])


    insert_query = "Insert Into tbl_standard_fields ( "
    colums = ""
    column_values = ""
    # Iterate keys 
    for key  in dct[0]:
        print(key)
        colums = colums + key + "," + "conf_" + key + ","
        val_arr = dct[0][key]     #   eg. "invoice_number": ["22352089-00", "54.37"]

        column_values = column_values + " '"+ str(val_arr.strip()) + "' , '0', "

    
    # Append other fields
    colums  = colums + "doc_id , process_id , created_date ) "
    column_values = column_values +  "'"+ doc_id + "','" + process_id + "','" + created_date + "'"

    prepare_query = insert_query + colums + " VALUES (" + column_values + ")"
    
    print(prepare_query)



def parse_lineitem_standard_fields(document_name,doc_id,process_id):

   
     
    created_date = "2022-10-10 0:20 PM"
    dct = extract_data["results"]["Line_Items"]
    #print(dct["colums"])

    tbl_col = dct["colums"]
    tbl_rows = dct["rows"]

     
    prepare_query = "INSERT INTO tbl_lineitem_standard_fields "
    tbl_columns = ""
    # for col in dct["colums"]:
    #     tbl_columns = tbl_columns + col + ","

    # Other Columns
    tbl_columns = tbl_columns + "description,amount,doc_id, process_id, file_name, created_date"


    # LINE ITEMS VALUE 
    line_item_rows = ""
    for lst_items in tbl_rows:     
        print(lst_items)   
        row_item = ""
        for val_items in lst_items:

            if val_items != "":
                row_item = row_item + "'" +val_items.strip() + "' , " 

        row_item = row_item +  "'"+ doc_id + "','" + process_id + "','" + document_name + "','"+ created_date + "'"
        line_item_rows = line_item_rows + "(" + row_item + "),"   
       
    prepare_query = prepare_query + "( " + tbl_columns + ") VALUES "  + line_item_rows
    
    print(prepare_query)

import json

class FakeDict(dict):
    def __init__(self, items): 
        self._items = items
    def items(self):
        return self._items



def search_price (items,name):
    for keyval in items:
        if name.lower() == keyval['question'].lower():
            return keyval
def obj_dict(obj):
    return obj.__dict__

def fetch_extracted_json():
    #obj_json =  [("question", "what is company name"), ("question", "sender account no"), ("question", "receiver account no"), ("question", "what is receiver name"), ("question", "sender zip code"), ("question", "Sender location"), ("question", "Sender tel no"), ("question", "Receiver Location"), ("question", "Receiver address"), ("question", "Receiver zip code"), ("question", "Receiver contact Name"), ("question", "what is delivery address"), ("question", "What is city name")]
    obj_json =  [("question", "what is company name"), ("question", "sender account no")]
    #obj_json =  ["what is company name","sender account no"]
    return obj_json

def test():
    array_of_tuples = fetch_extracted_json()
    json_question = FakeDict(dict(array_of_tuples))  
    print(json_question)
def dump():     
     
    items = fetch_extracted_json()  
    js = {}
    str_items = ""
    for i in items:
        str_items =  str_items + ',"{}" : "{}"'.format("question",i[1] )        
    
    dump  ="{"+str_items[1:] + "}"
    oo = json.dumps(dump)
    print(oo)
     
      
    

test()
#parse_standard_fields(extract_data,"1","1")
#parse_lineitem_standard_fields("sample.pdf","1","1")

