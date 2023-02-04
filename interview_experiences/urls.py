from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('home/add_exp/', views.add_exp, name = 'add_Exp'),
    path('home/all_exp/',views.all_exp,name = "allexp"),
    path('home/my_exp/',views.my_exp,name = "myexp"),
    path('home/PostComment/',views.PostComment,name = "myexp"),
    path('home/my_bookmarks/',views.my_bookmarks,name = "mybookmarks"),
    path('home/all_exp/<str:slug>/',views.expslug,name = "exp"),
    path('home/edit_exp/<str:slug>/',views.edit_exp,name = "edit_exp"),
    path('home/delete_exp/<str:slug>/',views.delete_exp,name = "delete_exp"),
    path('home/bookmark_exp/<int:pk>/',views.add_bookmark,name = "add_bookmark")
]
