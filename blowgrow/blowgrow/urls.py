"""blowgrow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application
from oscarapi.app import application as api
from zinnia.urls  import include, url
#from growblog.urls import include, url
#from growblog import views


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
    url(r'^$', templates.promotion.home.html, name='home'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^growblog/', include('zinnia.urls')), 
    url(r'^comments/', include('django_comments.urls')),
    url(r'^tinymce/filebrowser/', include('zinnia_tinymce.urls')),
    url(r'^api/', include(api.urls)),
]


from django.contrib.sitemaps.views import index 
from django.contrib.sitemaps.views import sitemap 
from zinnia.sitemaps import AuthorSitemap 
from zinnia.sitemaps import CategorySitemap 
from zinnia.sitemaps import EntrySitemap 
from zinnia.sitemaps import TagSitemap 

sitemaps = { 
    'tags': TagSitemap, 
    'blog': EntrySitemap, 
    'authors': AuthorSitemap, 
    'categories': CategorySitemap 
    
    } 
    
urlpatterns += [ 
    url(r'^sitemap.xml$', 
    index, 
    {'sitemaps': sitemaps}), 
    url(r'^sitemap-(?P<section>.+)\.xml$', 
    sitemap, 
    {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
]