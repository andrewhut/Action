from django.conf.urls import patterns, include, url

urlpatterns = patterns('actiondesign.ad.views',
    url(r'^$', 'home', name='home'),
    url(r'^logout/$', 'logout', name='logout'),
)
