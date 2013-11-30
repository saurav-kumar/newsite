from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('blogs.views',
        url(r'^$', 'main'),
        url(r'^(\d+)/$', 'post'),
        url(r'^add_comment/(\d+)/$', 'add_comment'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
