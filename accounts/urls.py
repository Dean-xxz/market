import accounts.apis
from django.conf.urls import url

urlpatterns = [
    url(r'^code/send/$', accounts.apis.send_code_api, name="code_send_api"),
    url(r'^user/query/$', accounts.apis.query_user_api, name="user_query_api"),    
    url(r'^code/verify/$', accounts.apis.verify_code_api, name="code_verify_api"),
    url(r'^userprofile/update/$', accounts.apis.update_userprofile_api, name="userprofile_update_api"),
    url(r'^info/create/$', accounts.apis.create_info_api, name="info_create_api"),
    url(r'^info/query/$', accounts.apis.query_info_api, name="info_query_api"),


]
