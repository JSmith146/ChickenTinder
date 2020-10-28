from django.shortcuts import render, redirect
from login_registration.models import *

# Create your views here
def index(request):
    if 'user_id' not in request.session:
        return redirect('/log_reg')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'main/index.html', context)

def logout(request):
    request.session.clear()
    return redirect('/log_reg')