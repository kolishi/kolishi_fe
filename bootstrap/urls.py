from django.conf.urls import patterns, include, url
from views import test
urlpatterns = patterns('',
                       url(r'^$',test),
)