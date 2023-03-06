from django.urls import path
from .import views
from vmapp.views import *

urlpatterns=[
   path('',views.index,name='index'),
   path('index',views.index,name='index'),
   path('sign-up',views.sign_up, name='sign_up'),
   path('add_vehicle_dtls',views.add_vehicle_dtls, name='add_vehicle_dtls'),
   path('update/<int:id>',views.update,name='update'),
   
  
]