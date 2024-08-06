from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm
from django.shortcuts import render,redirect,reverse

# Create your views here.

@login_required()
def home(request):
    return render(request, 'pages/home.html')

def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfully registered')
            return redirect(reverse('register'))
    return render(request, 'pages/register.html', {'form': form})


def buy_view(request):
    return render(request, 'pages/buy.html')

def user_view(request):
    return render(request, 'pages/user.html')