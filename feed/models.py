# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Project(models.Model):

    title = models.CharField(("Titulo"), max_length=100)
    description_short = models.CharField(("Descripción Corta"),
                                         max_length=255, blank=True)
    description = models.CharField(("Descripción"),
                                   max_length=1000, blank=True)
    cover = models.ImageField(upload_to='Projects_cover', blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
