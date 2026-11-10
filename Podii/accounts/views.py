from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from Podii.accounts.forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from Podii.accounts.selectors.user_selectors import get_user_by_id
from Podii.accounts.services.user_services import update_user_profile

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('event_list')


def profile_view(request, user_id):
    user = get_user_by_id(user_id)
    if not user:
        return render(request, '404.html', status=404)

    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name', ''),
            'last_name': request.POST.get('last_name', ''),
        }
        update_user_profile(user, data)
        return redirect('profile', user_id=user.id)

    context = {'profile_user': user}
    return render(request, 'accounts/profile.html', context)