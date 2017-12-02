from django.conf.urls import url
from formsapp import views

app_name = 'formsapp'

urlpatterns = [
    url(r'^$', views.index1, name='index1'),
    url(r'^index1/', views.index1, name='index1'),
    url(r'^formpage/', views.form_name_view,name='form_name'),
    url(r'^signup1/', views.SystemUsers,name='SystemUsers'),
    url(r'^relative/', views.relative,name='relative'),
    url(r'^other/', views.other,name='other'),
    url(r'^test/$', views.test1,name='test'),

]
