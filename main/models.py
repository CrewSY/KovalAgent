# -*- coding: utf-8 -*-
"""Models for main app of KovalAgent project."""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Equipment(models.Model):
    """Model that represents equipment."""

    class Meta:
        """Meta data of equipment."""

        verbose_name = u'Обладнання'
        verbose_name_plural = u'Обладнання'

    STATUS_CHOICES = (
        ('in_stock', u'Доступний на складі'),
        ('hired', u'У прокаті'),
        ('needs_repairs', u'Потребує ремонту'),
        ('under_repair', u'У ремонті',)
    )

    status = models.CharField(verbose_name=u'Статус',
                              max_length=24,
                              choices=STATUS_CHOICES,
                              blank=True,
                              null=True)
    title = models.CharField(verbose_name='Заголовок',
                             blank=True,
                             max_length=64)
    description = models.TextField(verbose_name=u'Опис', blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        """Render the equipment instance as a string."""
        return '%s - %s' % (self.title, self.status)


class EquipmentLog(models.Model):
    """Model that represents equipment log."""

    class Meta:
        """Meta data of equipment log."""

        verbose_name = u'Дія з обладнанням'
        verbose_name_plural = u'Дії з обладнанням'

    owner = models.OneToOneField(User,
                                 verbose_name=u'Користувач')
    iteam = models.ForeignKey(Equipment,
                              verbose_name=u'Обладнання')
    pre_status = models.CharField(verbose_name=u'Статус до',
                                  max_length=24)
    post_status = models.CharField(verbose_name=u'Статус після',
                                   max_length=24)
    date = models.DateTimeField(verbose_name=u'Дата',
                                default=timezone.now)

    def __str__(self):
        """Render the equipment log instance as a string."""
        return self.id
