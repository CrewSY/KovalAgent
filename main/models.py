# -*- coding: utf-8 -*-
"""Models for main app of KovalAgent project."""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Status(models.Model):
    """Model that represents status of equipment."""

    name = models.CharField(verbose_name=u'Стан',
                            max_length=48)

    def __str__(self):
        """Render the equipment status instance as a string."""
        return self.name

    class Meta:
        """Meta data of equipment status."""

        verbose_name = 'Стан обладнання'
        verbose_name_plural = 'Стан обладнання'


class Equipment(models.Model):
    """Model that represents equipment."""

    class Meta:
        """Meta data of equipment."""

        verbose_name = u'Обладнання'
        verbose_name_plural = u'Обладнання'

    status = models.ForeignKey(Status,
                               verbose_name=u'Стан')
    photo = models.ImageField(verbose_name=u'Фото',
                              blank=True,
                              null=True)
    title = models.CharField(verbose_name='Заголовок',
                             blank=True,
                             max_length=64)
    description = models.TextField(verbose_name=u'Опис',
                                   blank=True)

    def __str__(self):
        """Render the equipment instance as a string."""
        return '%s' % self.title


class EquipmentLog(models.Model):
    """Model that represents equipment log."""

    class Meta:
        """Meta data of equipment log."""

        verbose_name = u'Дія з обладнанням'
        verbose_name_plural = u'Дії з обладнанням'

    owner = models.ForeignKey(User,
                              verbose_name=u'Користувач')
    iteam = models.ForeignKey(Equipment,
                              verbose_name=u'Обладнання')
    pre_status = models.CharField(verbose_name=u'Стан до',
                                  max_length=48)
    post_status = models.CharField(verbose_name=u'Стан після',
                                   max_length=48)
    date = models.DateTimeField(verbose_name=u'Дата',
                                default=timezone.now)

    def __str__(self):
        """Render the equipment log instance as a string."""
        return '%s' % self.id
