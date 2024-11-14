# urls.py
from django.urls import path
from .views import (
    RegisterProfileView,
    login,
    LogoutView,
    FollowView,
    UnfollowView,
    ProfileDetailView,
    
)

urlpatterns = [
    path('register/', RegisterProfileView.as_view(), name='register'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('follow/<int:pk>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:pk>/', UnfollowView.as_view(), name='unfollow'),

]