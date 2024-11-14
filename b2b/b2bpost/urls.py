# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import B2BPostViewSet,createpost # Use the correct view name

urlpatterns = [
       path('api/b2bposts/',createpost, name ='post'),  
]
