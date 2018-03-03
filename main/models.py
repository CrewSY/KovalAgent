# -*- coding: utf-8 -*-
"""Models for main app of KovalAgent project."""

from django.db import models


class Equipment(models.Model):
    """Model that represents equipment."""

    class Meta:
        """Meta data of equipment."""

        verbose_name = u'Обладнання'
        verbose_name_plural = u'Обладнаня'

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
        """Render theequipment instance as a string."""
        return '%s - %s' % (self.title, self.status)
