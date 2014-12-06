from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'confession.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('bootstrap.urls')),
    url(r'^api/',include('conference.urls')),
    url(r'^boot/',include('bootstrap.urls'))
)
urlpatterns += staticfiles_urlpatterns()
