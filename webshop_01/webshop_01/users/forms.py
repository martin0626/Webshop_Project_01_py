from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.template.defaultfilters import capfirst

user_model = auth.get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = user_model
        fields = ('email',)

    email = forms.CharField(
        label=("Email Address"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "class": "form-control"}),
        strip=False,
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )

    # def __init__(self, request=None, *args, **kwargs):
    #     """
    #     The 'request' parameter is set for custom auth use by subclasses.
    #     The form data comes in via the standard 'data' kwarg.
    #     """
    #     self.request = request
    #     self.user_cache = None
    #     super().__init__(*args, **kwargs)
    #
    #     # Set the max length and label for the "username" field.
    #     self.username_field = user_model._meta.get_field(user_model.USERNAME_FIELD)
    #     username_max_length = self.username_field.max_length or 254
    #     self.fields["email"].max_length = username_max_length
    #     self.fields["email"].widget.attrs["maxlength"] = username_max_length
    #     if self.fields["email"].label is None:
    #         self.fields["email"].label = capfirst(self.username_field.verbose_name)
    #
    # def clean(self):
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #
    #     if email is not None and password:
    #         self.user_cache = authenticate(
    #             self.request, email=email, password=password
    #         )
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #
    #     return self.cleaned_data