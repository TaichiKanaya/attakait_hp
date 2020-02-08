"""attakait_hp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# 管理ページの文言設定
from hp import views

admin.site.site_title = 'あったかIT'
admin.site.site_header = 'コンテンツ管理'
admin.site.index_title = 'メニュー'

urlpatterns = [
    path('setting/', admin.site.urls),
    path('hp/', include('hp.urls')),
    url(r'^$', views.HomeView.as_view(), name="home"),
]

urlpatterns += staticfiles_urlpatterns()
