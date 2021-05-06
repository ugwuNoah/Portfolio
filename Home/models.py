from django.db import models


# What i'm good at model
class WhatImGoodAt(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


# MY Works model
class MyWork(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
