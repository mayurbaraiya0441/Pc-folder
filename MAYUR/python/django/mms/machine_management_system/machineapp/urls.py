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


# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







# user  
path('brand_show',views.brand_show, name='brand_show'),
path('brand_add/',views.brand_add,name='brand_add'),
path('brand_update/<int:id>',views.brand_update,name='brand_update'),
path('brand_delete/<int:id>',views.brand_delete,name='brand_delete'),
path('brand_status/<int:id>',views.brand_status,name='brand_status'),


# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







# user  
path('tax_show',views.tax_show, name='tax_show'),
path('tax_add/',views.tax_add,name='tax_add'),
path('tax_update/<int:id>',views.tax_update,name='tax_update'),
path('tax_delete/<int:id>',views.tax_delete,name='tax_delete'),
path('tax_status/<int:id>',views.tax_status,name='tax_status'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













