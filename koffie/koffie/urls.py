from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'article.views.index', name='home'),
    # url(r'^koffie/', include('koffie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #url(r'^login/', 'django.contrib.auth.views.login'),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
     # Serve static content.
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)
