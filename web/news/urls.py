
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user , name='login'),
    path('logout/', views.logout_user , name='logout'),
    path('register/', views.register_user , name='register'),    
    path('detail/<int:pk>', views.detail , name='detail'),    
    path('newpost/', views.newpost , name='newpost'),    
    path('savedata/', views.savedata , name='savedata'),   
    
      

   
]
