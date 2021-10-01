from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .form import UserLoginForm, UserRegisterForm, UserUpdateForm
User=get_user_model()

def login_view(request):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data['email']
        password=form.cleaned_data['password']
        user=authenticate(email=email,password=password)

        login(request, user)
        return HttpResponseRedirect(reverse('scraping:home'))
    return render(request,'accounts/login.html',{'form':form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('scraping:home'))
def register_login(request):
    form=UserRegisterForm(request.POST or None)
    if form.is_valid():
        new_user=form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return HttpResponseRedirect(reverse('accounts:login'))
    return render(request,'accounts/register.html',{'form':form})


def user_update_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                data=form.cleaned_data
                user.city=data['city']
                user.language=data['language']
                user.send_email=data['send_email']
                user.save()
                return HttpResponseRedirect(reverse('accounts:update'))
        else:
            form = UserUpdateForm(initial={'city': user.city, 'language': user.language,
                                           'send_email': user.send_email})
        return render(request, 'accounts/update.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('scraping:home'))
def delete_user(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method=='POST':
            qs=User.objects.filter(pk=user.pk)
            qs.delete()
    return HttpResponseRedirect(reverse('scraping:home'))
