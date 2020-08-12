from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import MyForm
from .forms import UserLoginForm
from django.contrib.auth import authenticate
from .models import Todolist, Organization
# Create your views here.
@login_required
def index(request):
    current_org = request.user.first_name
    todos = Todolst.objects.filter(organization=current_org)
    orgs = Organization.objects.all()
    context = {'todos': todos, 'orgs': orgs}
    return render(request, 'accounts/index.html', context)


def sign_up(request):
    context = {}
    form = MyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'accounts/index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    title = "Connection"
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        orga = form.cleaned_data.get("first_name")
        user = authenticate(username=username, password=password, email=email)
        login(request, user)
        todos = Todolist.objects.filter(company=orga)
        return render(request, 'accounts/index.html', {'todos': todos})
    return render(request, "login.html", {"form": form, "title": title})
