from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^$', 'article.views.index', name='home'),
    url(r'^tag/(?P<tagname>[a-zA-Z]{2,20})/$', 'article.views.browse_tag'),
    url(r'^add$', 'article.views.add_article'),
)
