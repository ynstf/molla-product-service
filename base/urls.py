from . import views
from django.urls import path

urlpatterns = [
    path('showproducts', views.product_list),
    path('showproducts/<int:pk>/', views.product_show),
    path('postproducts', views.product_create),

]