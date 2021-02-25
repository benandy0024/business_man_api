from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from.views import RegisterApiView,CustomAuthToken,UserLoginApiView
urlpatterns = [
    path(r'register', RegisterApiView.as_view(), name='auth'),
    path(r'login',  UserLoginApiView.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token)
]
