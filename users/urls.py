from django.urls import path


from users.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('delete/<int:pk>/', UserDeleteView.as_view()),
]
