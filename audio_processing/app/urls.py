from django.urls import path

# View References
from . import views
from . import views_documents
from . import views_audio
from . import views_classification
from . import views_extraction
from . import views_layout
from . import views_agent
from . import views_dashboard

# API Refrences
from . import api_views_documents
from . import api_views_extraction
from .import api_views_agent
from . import api_views_config
from . import api_views_classification
from . import api_views_audio

from . import api_views_user

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
 
    #Dashboard Page
    path('dashboard/', views_dashboard.index, name='dashboard'),

    #Layouts URLS
    path('layout/', views_layout.index, name='layout'),
    path('layout/add', views_layout.add, name='add_layout'),

    #Audio URLS    
    path('audio/', views_audio.index, name='media'),
    path('audio/upload', views_audio.upload, name='upload_document'),   
    path('audio/media', views_audio.media_files, name='media_files'),
    path('audio/processed', views_audio.processed, name='audio_processed'),  
    path('audio/analysis/<id>/', views_audio.analysis, name='analysis'), 
    

    # Classification
    path('classification/layout/', views_classification.index, name='classifier_layout'),
    path('classification/layout/add', views_classification.add, name='add_classification_layout'),
 
    
    #API CLASSIFICATION
    path('add_new_classifier', api_views_classification.add_new_classifier, name='add_new_classifier'),
    path('get_trained_model_list', api_views_classification.get_trained_model_list, name='get_trained_model_list'),
    path('raise_request_train_modal', api_views_classification.raise_request_train_modal, name='raise_request_train_modal'),


    #path('classification/layout/add', views_classification.add, name='add_classifier'),

    #Documents
    path('documents/', views_documents.index, name='document'),
    path('documents/upload', views_documents.upload, name='upload'),
    path('documents/check', views_documents.check_api_response, name='check_api_response'),   
    path('documents/processed', views_documents.processed, name='processed'),  
    
    # Extraction
    path('extraction/', views_extraction.index, name='extraction'),  
    path('extraction/processed', views_extraction.processed, name='processed_doc'),
    path('extraction/detail/<id>/', views_extraction.detail, name='extraction_detail'),



    #API Documents
    path('uploadfile', api_views_documents.uploadfile, name='uploadfile'),

    path('upload_api_check_file', api_views_documents.upload_api_check_file, name='upload_api_check_file'),

     
    
    
    #API AUDIO
    path('upload_audio_file', api_views_audio.upload_audio_file, name='upload_audio_file'),
    path('get_nlp_detail', api_views_audio.get_nlp_detail, name='get_nlp_detail'),
    
    #Layouts
    path('add_new_config', api_views_config.add_new_config, name='add_new_config'),
    path('add_new_field', api_views_config.add_new_field, name='add_new_field'),
    path('delete_field', api_views_config.delete_field, name='delete_field'),
    path('delete_layout', api_views_config.delete_layout, name='delete_layout'),
    
    path('api_layout_detail', api_views_config.api_layout_detail, name='api_layout_detail'),
    path('run_extraction', api_views_extraction.run_extraction, name='run_extraction'),
    path('run_audio_extraction', api_views_extraction.run_audio_extraction, name='run_audio_extraction'),

    # login / Registeration API
    path('login_user', api_views_user.login_user, name='login_user'),
    path('create_new_account', api_views_user.create_new_account, name='create_new_account'),
    path('get_processed_standard_item_detail', api_views_extraction.get_processed_standard_item_detail, name='get_processed_standard_item_detail'),
    path('get_processed_standard_line_item_detail', api_views_extraction.get_processed_standard_line_item_detail, name='get_processed_standard_line_item_detail'),


    #Agent View
    path('agent/', views_agent.index, name='agent'),
    path('agent/doc/<id>/', views_agent.document, name='agent_doc'), 
    path('agent/check', views_agent.check_question, name='check_question'),
    

    #Agent API View
    path('get_document_field_list', api_views_agent.get_document_field_list, name='get_document_field_list'),
    path('get_document_field_data', api_views_agent.get_document_field_data, name='get_document_field_data'),
    path('check_api', api_views_agent.check_api, name='check_api'),

]
