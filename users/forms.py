from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, error_messages= {"invalid": "Please, enter correct E-mail"})

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'country', 'city_or_district', 'account_role')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'country', 'city_or_district', 'account_role')