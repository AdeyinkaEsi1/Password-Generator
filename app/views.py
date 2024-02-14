from django.shortcuts import render, redirect
from app.forms import Password_gen_form, UserRegForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main import gen_pw
from .models import GeneratedPassword
from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):
    next_page = 'home'


def home(request):
    return render(request, 'home.html')



# gen_pw(length=12)

@login_required
def generate_password(request):
    history = GeneratedPassword.objects.filter(user=request.user).order_by('-created_at')[:10]
    if request.method == 'POST':
        form = Password_gen_form(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            password = gen_pw(length)
            GeneratedPassword.objects.create(user=request.user, password=password)
            messages.success(request, f'Newly generated password --> {password}')
            return redirect('generate_password')
    else:
        form = Password_gen_form()
    return render(request, 'generate_password.html', {'form': form, 'history': history})


def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome {username}')
            return redirect('login')
    else:
        form = UserRegForm
    return render(request, 'register.html/', {'form': form})

