from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib import staticfiles

urlpatterns=[
    path('home/',home,name="home"),
    path('index/',index,name="index"),
    path('emp_add/',add_emp,name="emp_add"),
    path('emp_del/<int:emp>/',emp_del,name="emp_del"),
    path('emp_edit/<int:emp>/',emp_edit,name="emp_edit"),
    path('emp_update/<int:emp>/',emp_update,name="emp_update")

]