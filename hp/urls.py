from django.urls import path

from hp import views
app_name='hp'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('about_me/', views.AboutMeView.as_view(), name="about_me"),
    path('portfolios/', views.PortfoliosView.as_view(), name="portfolios"),
    path('skills/', views.SkillsView.as_view(), name="skills"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
