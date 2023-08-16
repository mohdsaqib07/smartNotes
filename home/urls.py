from django.urls import path , include
from . import views


urlpatterns = [
    path("",views.HomeView.as_view(),name='Home'),
    path("login/",views.LoginInterfaceView.as_view(),name='login'),
    path('authorize/',views.Authorized.as_view(),name='Authorize'),
    path('logout/',views.LogoutIntefaceView.as_view(),name='logout'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]
