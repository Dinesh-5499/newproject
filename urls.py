from django.urls import path
from . import views 
urlpatterns = [
    path('',views.add_detail,name='add_detail'),
    path('all_cams',views.all_cams,name='all_cams')
]
