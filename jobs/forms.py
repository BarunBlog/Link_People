from django import forms

from .models import PostJobModel



class PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJobModel
        fields = ['Job_title', 'Company', 'Job_location', 'Employee_type', 'Description', 'Add_skills']

        help_texts = {
            'Description': "Add a clear description",
            'Add_skills': "Add skills to make your job more visible to the right candidates",
        }
        