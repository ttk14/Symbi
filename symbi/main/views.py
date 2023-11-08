from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import login

from posts.models import ActivityPost
from .models import SocialUser
from .forms import RegisterForm, LoginForm  # Import your form classes here

class RegisterOrLoginView(generic.View):
    template_name = "main/register.html"

    def get(self, request):
        login_form = LoginForm()  # Create an instance of the LoginForm class
        register_form = RegisterForm()  # Create an instance of the RegisterForm class
        return render(
            request,
            "main/register.html",
            {"login_form": login_form, "register_form": register_form},
        )

    def post(self, request):
        login_form = LoginForm(request.POST)  # Create an instance of the LoginForm with POST data
        register_form = RegisterForm(request.POST)  # Create an instance of the RegisterForm with POST data

        if "login" in request.POST:
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return HttpResponseRedirect(reverse("main:home"))
        elif "register" in request.POST:
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return HttpResponseRedirect(reverse("main:home"))

        return render(
            request,
            "main/register.html",
            {"login_form": login_form, "register_form": register_form},
        )

def home(request):
    template_name = "main/home.html"
    latest_posts_list = ActivityPost.objects.order_by("-timestamp")[:50]
    context = {
        "latest_posts_list": latest_posts_list,
    }
    return render(request, template_name, context)

class ProfileDetailsView(generic.DetailView):
    model = SocialUser
    template_name = "main/profile_details.html"
    context_object_name = "profile"
