from django.conf.urls import patterns, include, url
from views import get_name,thanks
urlpatterns = patterns('',
                       url(r'^$',get_name),
                       url(r'thanks/',thanks)
)