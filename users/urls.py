from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserCreateView, UserListView, LocationViewSet



urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateView.as_view()),
]


