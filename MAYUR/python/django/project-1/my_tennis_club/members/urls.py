from django.urls import path


# now import the views.py file into this code
from . import views
urlpatterns=[
path('',views.dashboard,name='dashboard'),

# user  
path('user_show',views.user_show, name='user_show'),
path('user_add/',views.user_add,name='user_add'),
path('user_update/<int:id>',views.user_update,name='user_update'),
path('user_delete/<int:id>',views.user_delete,name='user_delete'),
path('login',views.login,name='login'),




]
