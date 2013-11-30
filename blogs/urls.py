from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('blogs.views',
        url(r'^$','main'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
