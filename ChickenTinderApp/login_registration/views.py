from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'log_reg/index.html')

def register(request):
    if request.method == "GET":
        return redirect('/log_reg')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/log_reg')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/main')

def login(request):
    if request.method == "GET":
        return redirect('/log_reg')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/log_reg')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/main')

def logout(request):
    request.session.clear()
    return redirect('/log_reg')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/log_reg')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'log_reg/success.html', context)