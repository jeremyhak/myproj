from django.shortcuts import render,redirect
from django.contrib.auth.forms import (UserCreationForm,AuthenticationForm,
                                       UserChangeForm, PasswordChangeForm)
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile , Review
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm , SignUpForm , UserProfilePhoto , EditProfileForm , CommentsForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from . import forms
from django.db.models import Q
from .filters import ReviewFilter , ProfileFilter
from django.contrib.auth.decorators import login_required


@login_required(login_url = "/accounts/login/")
def edit_user(request):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=( 'phone', 'city', 'country','image',))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()

                    return redirect('accounts:profile')

        return render(request, "accounts/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied



@login_required(login_url = "/accounts/login/")
def edit_photo(request):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    user_form = UserProfilePhoto(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=( 'image',))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfilePhoto(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()

                    return redirect('accounts:profile')

        return render(request, "accounts/photo_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied






def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            user = request.user
            login(request, user)
            return redirect('articles:list')
    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html', {'form':form})


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})


def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')


@login_required(login_url = "/accounts/login/")
def my_profile_view(request, pk=None ):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/my_profile.html', args)

@login_required(login_url = "/accounts/login/")
def profile_view(request, pk=None ):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


#def edit_profile_view(request):

#    if request.method == 'POST':
#        form = EditProfileForm(request.POST, instance=request.user)

#        if form.is_valid():
#            form.save()
#            return redirect('accounts:profile')
#    else:
#        form = EditProfileForm(instance=request.user)
#        args = {'form':form}
#    return render(request, 'accounts/edit_profile.html', args)

@login_required(login_url = "/accounts/login/")
def change_password_view(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:change_password')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form':form})

@login_required(login_url = "/accounts/login/")
def reviews_create(request):
    if request.method == 'POST':
        form = forms.CommentsForm(request.POST, request.FILES)

        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.save()
    else:
        form = forms.CommentsForm()
    return render(request, 'accounts/create_review.html', {'form': form})
