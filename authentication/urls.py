from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.RegisterUser.as_view(), name="registration"),
]

