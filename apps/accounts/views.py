from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ProfileForm, ChangePasswordForm, UserForm
from .models import Profile

def get_user_profile(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            get_user_profile(user)
            login(request, user)
            print(f'user {user.phone_number} has successfully signed up')
            return redirect('home')
        print('An error occurred')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username=phone_number,
                password=password
            )

            if user is not None:
                login(request, user)
                print(f'user {phone_number} has successfully signed in')
                return redirect('home')

            form.add_error(None, 'Invalid phone number or password')
        print('An error occurred')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    print('user logged out')
    return redirect('home')

@login_required
def profile_view(request):
    profile = get_user_profile(request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    profile = get_user_profile(request.user)

    if request.method == "POST":
        user_form = UserForm(
            request.POST,
            instance=request.user,
        )
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(
            instance=request.user
        )
        profile_form = ProfileForm(
            instance=profile
        )
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request, 'accounts/profile-edit.html', context)

@login_required
def password_change_view(request):
    if request.method == "POST":
        form = ChangePasswordForm(
            request.user,
            request.POST
        )
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('profile')
    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'accounts/profile-edit.html', {'password_form': form})







