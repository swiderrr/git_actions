from django.urls import path
from api_post import views
from rest_framework.routers import DefaultRouter
from django.urls import include
from api_post.views import PostView



urlpatterns = [
    path('add', PostView),
]