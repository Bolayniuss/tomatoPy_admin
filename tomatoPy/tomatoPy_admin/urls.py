from django.conf.urls import patterns, include, url
from django.contrib import admin

import tvshows.urls
import movies.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tomatoPy_admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tvshows/', include(tvshows.urls)),
    url(r'^movies/', include(movies.urls)),
)
