# -*- coding: utf-8 -*-
from __future__ import unicode_literals,division

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from app import settings
from star_ratings.models import AbstractBaseRating





class UserProfile(models.Model):


    user = models.OneToOneField(User, related_name='user', null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=False, null=True)
    phone = models.CharField(max_length=20, blank=True, default='',null=True)
    city = models.CharField(max_length=100, default='', blank=True ,null=True)
    country = models.CharField(max_length=100, default='', blank=True ,null=True)

class Review(models.Model):


    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, default= None, null=True)


    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("accounts:reviews", kwargs ={"id": self.id})




def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
