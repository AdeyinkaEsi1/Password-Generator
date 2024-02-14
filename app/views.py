from django.shortcuts import render, redirect
import string, random
from .forms import Password_gen_form
from django.contrib import messages
# from main import get_password



def gen_pw(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_password(request):
    if request.method == 'POST':
        form = Password_gen_form(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            password = gen_pw(length)
            messages.success(request, f'Newly generated password --> {password}')
            return redirect('generate_password')
    else:
        form = Password_gen_form()
    return render(request, 'generate_password.html', {'form': form})




