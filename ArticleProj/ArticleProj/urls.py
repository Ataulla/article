from django.conf.urls import patterns, include, url
from django.contrib import admin
from ArticleApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ArticleProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<art_id>.*)/$', views.details, name='details'),
    url(r'^admin/', include(admin.site.urls)),
)

