from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import login

from posts.models import ActivityPost
from .models import SocialUser

# from .forms import SignUpForm, RegisterForm
from .forms import RegisterForm, LoginForm


class RegisterOrLoginView(generic.View):
    template_name = "main/register.html"

    def get(self, request):
        login_form = LoginForm
        register_form = RegisterForm
        return render(
            request,
            "main/register.html",
            {"login_form": login_form, "register_form": register_form},
        )

    def post(self, request):
        if "login" in request.POST:
            form = LoginForm(dataa=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return HttpResponseRedirect(reverse("main:home"))
        elif "register" in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return HttpResponseRedirect(reverse("main:home"))

        return render(
            request,
            "main/register.html",
            {"login_form": login_form, "register_form": register_form},
        )


# class RegisterView(generic.View):
#     def get(self, request):
#         return render(request, "main/register.html", {"form": RegisterForm})

#     def post(self, request):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return HttpResponseRedirect(reverse("main:home"))

#         return render(request, "main/register.html", {"form": form})


# class SignUpView(generic.CreateView):
#     template_name = "main/register.html"
#     form_class = SignUpForm
#     success_url = reverse_lazy("main:home")


# def home(request):
#     template_name = "main/home.html"
#     latest_posts_list = ActivityPost.objects.order_by("-timestamp")[:50]
#     context = {
#         "latest_posts_list": latest_posts_list,
#     }
#     return render(request, template_name, context)


# def sign_up(request):
#     template_name = "registration/signup.html"
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return HttpResponseRedirect(reverse("main:home"))
#     else:
#         form = SignUpForm()
#     return render(request, template_name, {"form": form})


# class ProfileDetailsView(generic.DetailView):
#     model = SocialUser
#     template_name = "main/profile_details.html"
#     context_object_name = "profile"

def home(request):
    template_name = "main/home.html"
    latest_posts_list = ActivityPost.objects.order_by("-timestamp")[:50]
    print(latest_posts_list)
    context = {
        "latest_posts_list": latest_posts_list,
    }
    return render(request, template_name, context)

class ProfileDetailsView(generic.DetailView):
    model = SocialUser
    template_name = "main/profile_details.html"
    context_object_name = "profile"