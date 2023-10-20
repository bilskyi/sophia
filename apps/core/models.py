from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(_("Subject"), max_length=50)
    description = models.TextField(_("Description"), blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='group_courses', verbose_name=_('Group'), null=True)
    owner = models.ManyToManyField(to='user.User', related_name='owner_courses', verbose_name=_('Owner'))

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    name = models.CharField(_('Group'), max_length=30)

    def __str__(self) -> str:
        return self.name