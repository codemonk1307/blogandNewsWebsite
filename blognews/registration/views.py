
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here

class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}! You are a member')
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    