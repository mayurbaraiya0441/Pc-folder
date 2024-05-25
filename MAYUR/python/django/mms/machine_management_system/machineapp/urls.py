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


# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# user  
path('subcategory_show',views.subcategory_show, name='subcategory_show'),
path('subcategory_add/',views.subcategory_add,name='subcategory_add'),
path('subcategory_update/<int:id>',views.subcategory_update,name='subcategory_update'),
path('subcategory_delete/<int:id>',views.subcategory_delete,name='subcategory_delete'),
path('subcategory_status/<int:id>',views.subcategory_status,name='subcategory_status'),






path('country_show',views.country_show, name='country_show'),
path('country_add/',views.country_add,name='country_add'),
path('country_update/<int:id>',views.country_update,name='country_update'),
path('country_delete/<int:id>',views.country_delete,name='country_delete'),
path('country_status/<int:id>',views.country_status,name='country_status'),




path('state_show',views.state_show, name='state_show'),
path('state_add/',views.state_add,name='state_add'),
path('state_update/<int:id>',views.state_update,name='state_update'),
path('state_delete/<int:id>',views.state_delete,name='state_delete'),
path('state_status/<int:id>',views.state_status,name='state_status'),




path('city_show',views.city_show, name='city_show'),
path('city_add/',views.city_add,name='city_add'),
path('city_update/<int:id>',views.city_update,name='city_update'),
path('city_delete/<int:id>',views.city_delete,name='city_delete'),
path('city_status/<int:id>',views.city_status,name='city_status'),




path('customer_show',views.customer_show, name='customer_show'),
path('customer_add/',views.customer_add,name='customer_add'),
path('customer_update/<int:id>',views.customer_update,name='customer_update'),
path('customer_delete/<int:id>',views.customer_delete,name='customer_delete'),
# path('customer_status/<int:id>',views.customer_status,name='customer_status'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



















