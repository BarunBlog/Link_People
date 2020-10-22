from django import forms

from .models import PostJobModel, PostJobPartTwoModel



class PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJobModel
        fields = ['Job_title', 'Company', 'Job_location', 'Employee_type']



class PostJobPartTwoForm(forms.ModelForm):
    class Meta:
        model = PostJobPartTwoModel
        fields = ['Description', 'Add_skills', 'Email_address']