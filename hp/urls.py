from django.urls import path

from hp import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('top/', views.TopView.as_view(), name="top"),
]
