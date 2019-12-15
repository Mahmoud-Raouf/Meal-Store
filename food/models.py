from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class Restaurant(models.Model):
    user = models.OneToOneField(User , verbose_name=_("User :"), on_delete=models.CASCADE)
    name = models.CharField(_("Name :"), max_length=50)
    phone = models.CharField(_("Number :"), max_length=50)
    address = models.CharField(_("Adrress :"), max_length=50)
    logo = models.ImageField(_("Logo :"), upload_to='logo_image')
    slug = models.SlugField(_("Slug :") , blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)
    

