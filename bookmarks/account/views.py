from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        # Check the validity of submitted data and log in a valid user or return an error message to
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid credentials")
    else:
        form = LoginForm()
    return render(request, "account/login.xhtml", {"form": form})


@login_required
def dashboard(request):
    return render(
        request,
        "account/dashboard.xhtml",
        {"section": "dashboard"},
    )
