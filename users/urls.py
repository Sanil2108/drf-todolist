from django.urls import path
from users.views import UserDetailView, UserTokenAuthenticationView, UserPasswordAuthenticationView

urlpatterns = [
    path('detail/', UserDetailView.as_view(), name = 'User Creation/Deletion'),
    path('token_auth/', UserTokenAuthenticationView.as_view(), name = 'User Token Authentication'),
    path('password_auth/', UserPasswordAuthenticationView.as_view(), name = 'User Password Authentication'),
]