from django.urls import path

from hp import views
app_name='hp'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('self_introduction/', views.SelfIntroductionView.as_view(), name="self_introduction"),
    path('portfolios/', views.PortfoliosView.as_view(), name="portfolios"),
    path('skills/', views.SkillsView.as_view(), name="skills"),
]
