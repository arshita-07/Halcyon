from django.contrib import admin
from django.urls import path
from app import views
from .views import *

urlpatterns = [
    path('home/', views.home, name="home"),
    path('done/', views.done, name="done"),
    path('resource_list/', ResourceListView.as_view(), name="list"),
    path('detail/<int:pk>/',ResourceDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',ResourceUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',ResourceDeleteView.as_view(),name='delete'),
    path('create/',ResourceCreateView.as_view(),name='create'),
    path('apply/<int:pk>/', views.apply, name="apply"), 
    path('myapplications/',views.myapplications, name="myapplications"),
    path('applicationforresource/<int:pk>',views.applicationforresource,name ="applicationforresource")
]