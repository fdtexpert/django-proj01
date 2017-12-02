from django.conf.urls import url
from amtesting_app import views

urlpatterns = [
    url(r'^$', views.index, name='indexprv'),
]
