from django.urls import path
from .views import RegisterView, UserView, ChangePassword

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user', UserView.as_view()),
    path('change-password', ChangePassword.as_view())
]