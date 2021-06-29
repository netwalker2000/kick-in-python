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
from django.contrib import admin

import productApp.views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Product APIs for entry task')

urlpatterns = [
    url(r'^$', schema_view),
    url('products/<int:id>/comments', productApp.views.comments),
    url('products/<int:id>', productApp.views.query_product_detail),
    url('products/', productApp.views.query_list_no_param),
]
