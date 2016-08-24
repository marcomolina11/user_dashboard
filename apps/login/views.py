from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
from .forms import RegisterForm, LoginForm

# Login and reg at homepage
def index(request):
    request.session.clear()
    context = {
        'regform': RegisterForm,
        'loginform': LoginForm
    }
    return render(request, 'login/index.html', context)

# Submit registration form
def register(request):
    regstatus = User.userManager.register(**request.POST)
    if regstatus[0]:
        return redirect(reverse('dashboard:index_admin'))
    else:
        for message in regstatus[1]:
            messages.warning(request, message)
        return redirect(reverse('login:new_admin'))

# Submit login form
def login(request):
    loginstatus = User.userManager.login(request.POST['email'], request.POST['password'])
    print "MAYBE HERE?!"
    if loginstatus[0]:
        request.session['user_id'] = loginstatus[1]
        print "THSI SHOULD WORK"
        return redirect(reverse('dashboard:index'))
    else:
        messages.warning(request, loginstatus[1])
        print "DIDNT WORK SRY"
        return redirect(reverse('login:index'))
