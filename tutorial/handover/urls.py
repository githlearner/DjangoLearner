from django.conf.urls import url
from. import views

urlpatterns =[

    url(r'^newevent/$', views.new_event, name='current'),
    url(r'^CurrentHO/$', views.current_handover, name='currentho')


]