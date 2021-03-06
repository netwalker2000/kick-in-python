"""productProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import productApp.views
import commentApp.views
import user.views

urlpatterns = [
    url(r'^products/(?P<id>\d+)/comment$', commentApp.views.create_comment),
    url(r'^products/(?P<id>\d+)/comments$', commentApp.views.comments),
    url(r'^products/(?P<id>\d+)$', productApp.views.query_product_detail),
    url(r'^products/$', productApp.views.query_product_list),
    url(r'^users$', user.views.user_register),
    url(r'^users/validation$', user.views.user_login),
]
