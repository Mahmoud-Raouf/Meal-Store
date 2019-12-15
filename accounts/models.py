from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User , verbose_name=_("User :"), on_delete=models.CASCADE)
    slug = models.SlugField(_("Slug :"), blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254)
    bio = models.TextField()
    image = models.ImageField(_("Image :"), upload_to='Profile_imge')
    country = CountryField(_("Country :"))
    address = models.CharField(_("Address :"), max_length=50)
    is_superuser = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    joindate = models.DateTimeField(_("Join Date :"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' %(self.user.username)

    # def get_absolute_url(self):
    #     return reverse("Profile_detail", kwargs={"slug": self.slug})

def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



