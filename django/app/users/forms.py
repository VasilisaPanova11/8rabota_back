from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .utils import THEME_CHOICES, LANG_CHOICES


class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]


class SettingsForm(forms.Form):
    theme = forms.ChoiceField(choices=THEME_CHOICES, label="Тема", required=True)
    lang = forms.ChoiceField(choices=LANG_CHOICES, label="Язык", required=True)
