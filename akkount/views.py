from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.views.generic import UpdateView

from.models import Profile
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "username yoki parol xato ")
            return redirect('/akkount/login/')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:


        form = UserCreationForm()

    return render(request, 'sign_up.html', {'form': form})
def home(request):
    return render(request, 'home.html')
def profileView(request):
    user=request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user,role='user')
    return render(request, 'profile.html', {'profile': profile})

class ProfileEdit(UpdateView):
    model = Profile
    fields = ['ism','familiyasi','telefon','manzil', 'img']
    template_name = 'profile_edit.html'
    success_url = '/akkount/profile/'
