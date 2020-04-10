from django.urls import path
from users.views import UserDetailView, UserAuthenticationView

urlpatterns = [
    path('detail/', UserDetailView.as_view(), name = 'User Creation/Deletion'),
    path('auth/', UserAuthenticationView.as_view(), name = 'User Authentication'),
]