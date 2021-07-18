from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apioverview, name ='apioverview'),
    #path('list/', views.ShowAll,name='List')
    path('product-list/', views.ShowAll, name ='product_list'),
    path('product-detail/<int:ex>/', views.viewproduct, name ='product_details'),
    path('product-create/', views.createproduct, name ='cerate_product'),
]
