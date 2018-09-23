#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect ,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Article
from .models import PointOfInterest
from .forms import GetLoc , CreatePosts , PickDrop
from .filters import ArticleFilter
from formtools.wizard.views import SessionWizardView
from django.views.generic import TemplateView
from app import settings
from django.core.files.storage import FileSystemStorage
import os
from decimal import Decimal, DecimalException
from django.views import generic
from accounts.models import UserProfile
from django.contrib.auth.models import User








def article_list(request):
    articles = Article.objects.all().order_by('date');
    pk = request.user.pk


    query = request.GET.get("q")
    if query:
        articles = articles.filter(
                                Q(title__icontains = query)|
                                Q(description__icontains = query)|
                                Q(worth__icontains = query)
                                    ).distinct()
    return render(request, 'articles/article_list.html',{'articles':articles})

@login_required(login_url = "/accounts/login/")
def filter(request):
    article_list = Article.objects.all()
    article_filter = ArticleFilter(request.GET, queryset=article_list)
    return render(request,'articles/article_filter.html', {'filter': article_filter})


@login_required(login_url = "/accounts/login/")
def article_detail(request, id=None):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html',{ 'article':article })




FORMS = [("step1", forms.CreatePosts),
         ("step2", forms.PickDrop)
         ]

TEMPLATES = {"0": "articles/article_create.html",
             "1": "articles/location_create.html"
            }



class PostCreateWizard(SessionWizardView):
    instance = None

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    #Returns an object which will be passed to the form for `step`
    #as `instance`. If no instance object was provided while initializing
    #the form wizard, None will be returned

    def get_form_instance( self, step ):
        if self.instance is None:
            self.instance = Article()
        return self.instance


    def done(self, form_list, **kwargs):

        self.instance.author = self.request.user

        self.instance.save()
        return redirect('articles:list')






def article_delete(request, id=None):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('articles:list')


def pickup_create(request):
    if request.method == 'POST':
        form = forms.PickDrop(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.PickDrop()
    return render(request, 'articles/location_create.html', {'form': form})


#def pickup_list(request):
#    pickups = PointOfInterest.objects.all()
    #return render(request, 'poi_list.html', {'pois': pois})


def pickup_detail(request, id=None):
    pick = get_object_or_404(Article, id=id)
    return render(request, 'articles/location_pickup_detail.html',{ 'pick':pick })


@login_required(login_url = "/accounts/login/")
def calander(request):

    if request.method == 'POST':
        form = forms.TestCal(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = id.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.TestCal()
    return render(request, 'articles/calander.html', {'form': form})



@login_required(login_url = "/accounts/login/")
def my_posts(request):

    #if request.author.is_authenticated():

    articles = Article.objects.filter(author=request.user);
    return render(request, 'articles/my_posts.html',{ 'articles':articles })
