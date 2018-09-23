# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile ,Review



admin.site.register(UserProfile)
admin.site.register(Review)
