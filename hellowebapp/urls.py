from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^posts/(?P<slug>[-\w]+)/$', 'collection.views.post_detail', name='post_detail'),
    url(r'^posts/(?P<slug>[-\w]+)/edit/$','collection.views.edit_post', name='edit_post'),

    url(r'^admin/', include(admin.site.urls)),
)