from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView

from netaun_app.forms import CustomUserCreationForm


class HomeView(TemplateView):
    template_name = 'index.html'


class SignUpView(View):
    def get(self, request):
        f = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': f})

    def post(self, request):
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')


# def signup(request):
#     if request.method == 'POST':
#         f = CustomUserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('signup')
#     else:
#         f = CustomUserCreationForm()
#
#     return render(request, 'signup.html', {'form': f})
