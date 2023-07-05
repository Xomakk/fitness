from django.urls import path

from accounts import views

urlpatterns = [
    # path('account', views.buy(), name="account"),
    # path('programs', views.logout_user, name='programs'),
    path('buy/', views.buy, name='buy'),
    path('profile/', views.profile, name='profile'),
]
