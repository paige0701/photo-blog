"""paigegram URL Configuration

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
from django.contrib.auth import views

from photoblog.views import notloggedin, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    # If you are not logged in ~
    url(r'^notloggedin/$', notloggedin, name='notloggedin'),

    # Home
    url(r'^$', home, name='home'),

    # Login
    url(r'^login/$',views.login, {'template_name':'auth/login.html'}, name='login'),

    # Register
    # url(r'^register/$', views, )

]
