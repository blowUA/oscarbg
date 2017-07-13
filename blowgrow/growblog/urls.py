# -*- coding: utf-8 -*-

from django.conf import settings

from django.contrib import admin

from django.conf.urls import url

from django.conf.urls import include

from django.conf.urls import patterns





urlpatterns = patterns(
    url(r'^$', RedirectView.as_view(url='/growblog/', permanent=True)),
    url(r'^growblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),

]


