from django.urls import path
from . import views

urlpatterns = [

        path('', views.home, name='home'),
        path('item/<slug:alias>/', views.item, name='item'),
        path('shipping/', views.shipping, name='shipping'),
        path('about/', views.about, name='about'),
        path('contacts/', views.contacts, name='contacts'),
        path('<slug:alias>/', views.get_category, name='get_category'),
        path('item/addcomment/<slug:alias>/', views.addcomment, name='add_comment'),

]

