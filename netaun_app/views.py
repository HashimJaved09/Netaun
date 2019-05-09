from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView

from netaun_app.forms import CustomUserCreationForm, LoginForm


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

        messages.error(request, 'Please fill all fields')
        return redirect('signup')


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm()
        if form.is_valid():
            form.save()

            return redirect('home')


class ContactUsView(TemplateView):
    template_name = 'contact.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class AboutUsView(TemplateView):
    template_name = 'about.html'
