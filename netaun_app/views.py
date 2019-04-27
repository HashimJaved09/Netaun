from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from netaun_app.forms import CustomUserCreationForm


def index(request):

    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')
    else:
        f = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': f})
