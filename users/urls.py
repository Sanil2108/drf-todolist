from django.urls import path
from users.views import UserDetailView, UserAuthenticationView

urlpatterns = [
    path('', UserDetailView.as_view(), name = 'User Detail'),
    path('auth/', UserAuthenticationView.as_view(), name = 'User Authentication'),
]