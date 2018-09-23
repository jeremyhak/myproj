from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from string import Template
from django.utils.safestring import mark_safe
from .models import UserProfile ,Review







class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfilePhoto(forms.ModelForm):
    class Meta:
        model = User
        fields = []


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )
