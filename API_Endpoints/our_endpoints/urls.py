from django.urls import path
from . import views

from django.urls import path
#from our_endpoints.views import get_current_server_time, upload_file, check_connection, save_json_to_file,delete_file, delete_filecurl, update_file, AddView, AddViewcurl, SubView, DivView, MultiView
from our_endpoints.views import upload_file, check_connection, save_json_to_file,delete_file, delete_filecurl, update_file, AddView, AddViewcurl, SubView, DivView, MultiView

urlpatterns = [
#  path('', views.home, name='home'),
#  path('server_time/', get_current_server_time),
  path('upload_file/', upload_file),
  path('status2/', check_connection),
  path('save_json_to_file/', save_json_to_file),
  path('delete_file/', delete_file),
  path('delete_file/curl/',delete_filecurl),
  path('update_file/', update_file),
  path('addcurl/', AddViewcurl.as_view()),
  path('', views.contact),
  path('add/', AddView.as_view(), name='add'),
  path('sub/', SubView.as_view(), name='sub'),
  path('div/', DivView.as_view(), name='div'),
  path('multi/', MultiView.as_view(), name='multi')

]

app_name = 'our_endpoints'
