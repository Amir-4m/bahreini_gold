from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=120)
    slug = models.SlugField(verbose_name=_('slug'), unique=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('name'), max_length=120, blank=False)
    code = models.CharField(_('code'), max_length=120, blank=False)
    image = models.ImageField(_('image'), upload_to='products/images', null=True, blank=True)
    description = models.TextField(_('description'), default='description')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    slug = models.SlugField(verbose_name=_('slug'), unique=True)
    weight = models.CharField(_('weight'), max_length=120, blank=False)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)
