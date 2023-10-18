from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(_("Subject"), max_length=50)
    description = models.TextField(_("Description"),)
    owner = models.ManyToManyField(to='user.User', related_name='courses', verbose_name=_('Owner'))


class Group(models.Model):
    name = models.CharField(_('Group'), max_length=30)
