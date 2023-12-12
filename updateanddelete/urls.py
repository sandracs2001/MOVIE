from django.contrib import admin
from django.urls import path
from updateanddelete import views
app_name = 'updateanddelete'

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('somewhere<int:p>',views.somewhere,name='somewhere'),
    path('areyousure/<int:p>',views.areyousure,name='areyousure'),
    path('update/<int:p>',views.update,name='update'),
    path('delete/<int:p>',views.delete,name='delete')
]