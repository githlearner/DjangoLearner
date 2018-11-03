from django.conf.urls import url
from . import views
from django.contrib.auth.views import login , logout
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login , {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout , {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)/edit/$', views.edituser_profile, name='edituser'),
    url(r'^profile/$', views.profile, name='profile')
]