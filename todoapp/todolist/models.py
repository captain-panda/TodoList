# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class TodoList(models.Model):
    title = models.CharField(max_length = 250)
    content = models.TextField(blank = True)
    created = models.TimeField(default = timezone.now().strftime("%Y-%m-%d"))
    due_date = models.TimeField(default = timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default = "general")

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return self.title