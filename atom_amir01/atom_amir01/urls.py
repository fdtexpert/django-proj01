"""atom_amir01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
#from django.contrib.admin import pa
from django.conf.urls import url
from django.conf.urls import include
#from amtesting_app import views
from formsapp import views as v1
from fdtusers import views as v2

urlpatterns = [
    url(r'^$', v1.index1, name='index1'),
    url(r'^index$', v1.index1, name='index'),
    url(r'^amtest/', include('amtesting_app.urls')),
    url(r'^formsapp/', include('formsapp.urls')),
    url(r'^fdtuser/', include('fdtusers.urls')),
    url('admin/', admin.site.urls),
    url(r'^logout/$', v2.user_logout, name='logout'),
    url(r'^special/$', v2.special, name='special')
]
