#!/usr/bin/python
# -*- coding: utf-8 -*-
# mydata/models.py
""" Mydata models page """

from django.db import models

class Mybio(models.Model):
    """Define fields in Mybio model"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    bio = models.CharField(max_length=200)
    contacts = models.CharField(max_length=50)
    date_of_birth = models.DateField(verbose_name = "Date of birth")


    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class AuthRequest(models.Model):
    """Define fields in AuthRequest model"""
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)


