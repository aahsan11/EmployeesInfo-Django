
from . import views
from django.urls import path

urlpatterns=[
    path('',views.home, name='home'),
    path('AddEmployee', views.AddEmployee, name='AddEmployee'),
    path(r'^DeleteEmployee/?q<id>\d+)/$', views.DeleteEmployee, name='DeleteEmployee'),
    path(r'UpdateEmployee/?q<id>\d+)/$', views.UpdateEmployee, name='UpdateEmployee'),
    path('SaveEmployee', views.SaveEmployee, name='SaveEmployee'),
    path(r'^FinalUpdate/?q<id>\d+)/$', views.FinalUpdate, name='FinalUpdate')
    


]