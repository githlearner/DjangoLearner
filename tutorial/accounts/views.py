from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm,ProfileForm
from django.contrib.auth.models import User
from .models import CustomProfileModel



def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            #user.profile.city = user_form.cleaned_data.get('city')
            #user.profile.description = user_form.cleaned_data.get('description')
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/account/profile')

    else:
        user_form = RegistrationForm()
        profile_form = ProfileForm()

    args = {'user_form': user_form , 'profile_form':profile_form}
    return render(request, 'accounts/reg_form.html',args)


def profile(request):

    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edituser_profile(request,username):
    custom_detail = CustomProfileModel.objects.get(user__username=username)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,instance=custom_detail)
        if profile_form.is_valid():
            profile_form.full_clean()
            profile_form.save()
            user_detail = User.objects.get(username=username)
            custom_detail = CustomProfileModel.objects.get(user__username=username)
            args = {'user': user_detail, 'custom_user': custom_detail}
            return render(request, 'accounts/user_profile.html', args)
    else:
        profile_form = ProfileForm(instance=custom_detail)
        args = {'profile_form': profile_form}
        return render(request, 'accounts/edit_form.html', args)

def get_user_profile(request, username):
    user_detail = User.objects.get(username=username)
    custom_detail = CustomProfileModel.objects.get(user__username=username)
    args ={'user': user_detail,'custom_user':custom_detail}
    return render(request,'accounts/user_profile.html', args)


