from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SocialUser

# from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholder": "First Name"})
    )
    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholder": "Last Name"})
    )
    email = forms.EmailField(
        max_length=254,
        help_text="Please Enter Your NYU Email",
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )

    class Meta:
        model = SocialUser
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("nyu.edu"):
            raise forms.ValidationError("Only NYU Students are Allowed to Sign Up.")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        help_text="Please Enter Your NYU Email",
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    class Meta:
        model = SocialUser
        fields = ("email", "password")


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(required=True)
#     date_of_birth = forms.DateField(
#         widget=forms.SelectDateWidget(years=range(1970, 2030)), required=True
#     )
#     pronouns = forms.ChoiceField(choices=SocialUser.PRONOUN_CHOICES, required=True)

#     class Meta:
#         model = SocialUser
#         fields = [
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2",
#             "username",
#             "date_of_birth",
#             "pronouns",
#         ]

#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         if SocialUser.objects.filter(username=username).exists():
#             raise forms.ValidationError(
#                 "This username is already taken. Please choose a different one."
#             )
#         return username


# class SignInUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = SocialUser
#         fields = [
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2",
#             "username",
#             "date_of_birth",
#             "pronouns",
#         ]
