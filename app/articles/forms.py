from django import forms
from django.db import models
from . import models
from .models import Article
from .models import PointOfInterest
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField




class CreatePosts(forms.ModelForm):

    deliver_on = forms.DateField(widget = forms.SelectDateWidget())

    class Meta:
        model = models.Article
        fields = ['title', 'description',
                  'image', 'phone','worth','deliver_on',]

#    def save():

#        deliver_on = self.cleaned_data['deliver_on']


class PickDrop(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['pickup', 'dropat',]






class GetLoc(forms.ModelForm):
    class Meta:
        model = models.PointOfInterest
        fields = ['address','position',]
