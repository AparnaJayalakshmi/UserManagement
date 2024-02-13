from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.signup,name='signup'),
    path('loginPage/',views.loginPage,name='loginPage'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('home/',views.home,name='home'),
    path('createuser/',views.createuser,name='createuser'),
    path('update_user/<int:user_id>/', views.update_user, name='updateUser'),
    path('deleteuser/<int:user_id>/',views.delete_user,name='delete_user')

]