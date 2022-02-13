from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing, name='landing'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutuser, name='logout'),
    path('home/', views.home, name='home'),
    path('takehome/', views.takehome, name='takehome'),
    path('info/<str:pk>/', views.info, name='info'),
    path('post/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('updateBook/<str:pk>', views.updateBook, name='edit-book'),
    path('deleteBook/<str:pk>', views.deleteBook, name='delete-book'),
    path('redirect/', views.redirectt, name='redirectt'),
    
    
    
]