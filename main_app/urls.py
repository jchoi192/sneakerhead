from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sneakers/', views.sneakers_index, name='index'),
    path('sneakers/<int:sneaker_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),    
    path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
    
    path('accessories/', views.accessories_index, name='accessories_index'),
    path('accessories/<int:accessory_id>/', views.accessories_detail, name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),

    
]