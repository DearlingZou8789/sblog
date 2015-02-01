from django.conf.urls import patterns, include, url
from django.contrib import admin
from sblog1.views import current_time,current_time2,hours_ahead
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sblog.views.home', name='home'),
    url(r'^datetime/$', current_time),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^datetime/$', current_time),
    url(r'^datetime2/$', current_time2),
    url(r'^datetime/plus/(\d{1,2})/$', hours_ahead),
)
