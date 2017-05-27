# -*- coding: utf-8 -*-


from zinnia.urls import include, urls

growblog_urls = ([ url(r'^', include('zinnia.urls.capabilities')), url(r'^search/', include('zinnia.urls.search')), url(r'^sitemap/', include('zinnia.urls.sitemap')), url(r'^trackback/', include('zinnia.urls.trackback')), url(r'^growblog/tags/', include('zinnia.urls.tags')), url(r'^growblog/feeds/', include('zinnia.urls.feeds')), url(r'^growblog/random/', include('zinnia.urls.random')), url(r'^growblog/authors/', include('zinnia.urls.authors')), url(r'^growblog/categories/', include('zinnia.urls.categories')), url(r'^growblog/comments/', include('zinnia.urls.comments')), url(r'^growblog/', include('zinnia.urls.entries')), url(r'^growblog/', include('zinnia.urls.archives')), url(r'^growblog/', include('zinnia.urls.shortlink')), url(r'^growblog/', include('zinnia.urls.quick_entry')) ], 'zinnia') url(r'^', include(blog_urls))