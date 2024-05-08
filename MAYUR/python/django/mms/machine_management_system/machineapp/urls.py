from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

path('dashboard',views.dashboard,name='dashboard'),


#login,logout
path('',views.user_login,name='user_login'),
path('user_logout',views.user_logout,name='user_logout'),





# user  
path('category_show',views.category_show, name='category_show'),
path('category_add/',views.category_add,name='category_add'),
path('category_update/<int:id>',views.category_update,name='category_update'),
path('category_delete/<int:id>',views.category_delete,name='category_delete'),
path('category_status/<int:id>',views.category_status,name='category_status'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




