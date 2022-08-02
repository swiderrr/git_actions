from django.urls import path, include
from api_get import views


urlpatterns = [
    path('', views.index)
]