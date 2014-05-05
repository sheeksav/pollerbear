from django.conf.urls import patterns, include, url
from generic.views import HomeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home') # URLconf for homepage
)
