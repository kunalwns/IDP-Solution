from pdf2image import convert_from_path
import os
import cv2
from PIL import Image
import pytesseract



def pdf_to_image_convert(file_name,source_loaction_dir,output_dir):
    
   
    without_ext = os.path.splitext(file_name)[0].replace(" ", "_")
    file_location =  os.path.join(source_loaction_dir,file_name)
    output_path = os.path.join(output_dir)

    pages = convert_from_path(file_location, 350)

    i = 1
    for page in pages:
        image_name = os.path.join(output_path,"page_" + str(i) + ".jpg")
        page.save(image_name, "JPEG")
        i = i+1