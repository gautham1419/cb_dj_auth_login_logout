from django.shortcuts import render,redirect,reverse
from accounts.forms import CustomUserCreationForm


def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfully registered')
            return redirect(reverse('register'))
    return render(request, 'pages/register.html', {'form': form})
# Create your views here.
def home(request):
    return render(request,'pages/home.html')