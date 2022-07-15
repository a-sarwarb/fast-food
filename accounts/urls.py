from django.urls import path
from .views import SignUpView, UserProfileView, ProfileUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('edit/', ProfileUpdateView.as_view(), name='profile_edit')
]