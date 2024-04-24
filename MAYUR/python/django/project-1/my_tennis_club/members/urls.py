from django.urls import path


#now import the views.py file into this code
from . import views
urlpatterns=[
path('',views.index, name='index'),
path('add/',views.add,name='add'),
path('update/<int:id>',views.update,name='update'),
path('delete/<int:id>',views.delete_user,name='delete'),
path('dashboard/',views.dashboard,name='dashboard'),




]
