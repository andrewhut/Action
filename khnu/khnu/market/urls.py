from django.conf.urls import patterns, include, url

urlpatterns = patterns('khnu.market.views',
    url(r'^$', 'home', name='home'),
    url(r'^logout/$', 'logout', name='logout'),
)
