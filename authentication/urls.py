from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("api/register/", views.register, name="register"),
    path("api/login/", views.login, name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]