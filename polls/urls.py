from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'(?P<poll_id>\d+)/vote/$', 'vote'),
)   # no need to append polls.views now in url()

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
