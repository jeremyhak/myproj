from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from geoposition.fields import GeopositionField
from django.contrib.admin.widgets import AdminDateWidget






class Article(models.Model):
    title = models.CharField(max_length = 100)
    pickup = GeopositionField()
    dropat = GeopositionField()
    description = models.TextField('Description')
    date = models.DateTimeField(auto_now_add = True)
    worth = models.IntegerField('worth($)',default=0)
    image = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default= None, null=True)
    phone = models.IntegerField(default=0 )
    #deliver_on = models.TimeField(auto_now_add = False, default= None, null=True)





    def __str__(self):
        return self.title


    def snippet(self):
        return self.description[:70]+ '...'

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs ={"id": self.id})







class PointOfInterest(models.Model):
    address = models.CharField(max_length=100)
    position = GeopositionField()

    def get_absolute_url_map(self):
        return reverse("articles:map", kwargs ={"id": self.id})
