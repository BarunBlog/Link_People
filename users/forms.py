from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, error_messages= {"invalid": "Please, enter correct E-mail"})
    


    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'country', 'city_or_district')


    def signup(self, user):
        profile = CustomUser()
        profile.save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()

        user.profile = profile
        profile.user = user

        user.country = self.cleaned_data['country']
        user.city_or_district = self.cleaned_data['city_or_district']
        profile.save()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'country', 'city_or_district')