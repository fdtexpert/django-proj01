from django.conf.urls import url
from fdtusers import views

app_name = 'fdtusers'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),

]
