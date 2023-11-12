from uuid import uuid4
from django.db import models
from .utils import generate_short_string
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(_("Subject"), max_length=50)
    description = models.TextField(_("Description"), blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='group_courses', verbose_name=_('Group'))
    owner = models.ManyToManyField(to='user.User', related_name='owner_courses', verbose_name=_('Owner'))

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    name = models.CharField(_('Group'), max_length=30)
    link_id = models.CharField(_('Link Id'), max_length=6)

    def save(self, *args, **kwargs):
        if not self.link_id:
            while True:
                link_id = generate_short_string()
                if not Group.objects.filter(link_id=link_id).exists():
                    self.link_id = link_id
                    break
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.name