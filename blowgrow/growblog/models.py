"""Category model for Zinnia"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.apps import apps
from django.conf import settings
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager
from zinnia.managers import entries_published
from zinnia.managers import EntryRelatedPublishedManager


@python_2_unicode_compatible
class Category(MPTTModel):
   title = models.CharField( _('title'), max_length=255)
   slug = models.SlugField( _('slug'), unique=True, max_length=255,
help_text=_("Used to build the category's URL."))
description = models.TextField(
_('description'), blank=True)
parent = TreeForeignKey(
'self',
related_name='children',
null=True, blank=True,
on_delete=models.SET_NULL,
verbose_name=_('parent category'))
objects = TreeManager()
published = EntryRelatedPublishedManager()
def entries_published(self):
 return entries_published(self.entries)
@property
def tree_path(self):
 if self.parent_id: 
   return '/'.join(
[ancestor.slug for ancestor in self.get_ancestors()] +
[self.slug])
return self.slug
@models.permalink
def get_absolute_url(self):
  return ('growblog:category_detail', (self.tree_path,))
def __str__(self):
  return self.title
class Meta:
  ordering = ['title']
  verbose_name = _('category')
  verbose_name_plural = _('categories')
class MPTTMeta:
  order_insertion_by = ['title']
def safe_get_user_model():
  user_app, user_model = settings.AUTH_USER_MODEL.split('.')
    return apps.get_registered_model(user_app, user_model)
class AuthorPublishedManager(models.Model):
  published = EntryRelatedPublishedManager()
class Meta:
  abstract = True
@python_2_unicode_compatible
class Author(safe_get_user_model(),
AuthorPublishedManager):
def entries_published(self):
  return entries_published(self.entries)
@models.permalink
def get_absolute_url(self):
  return ('growblog:author_detail', [self.get_username()])
def __str__(self):
  return self.get_full_name() or self.get_username()
class Meta:
  proxy = True