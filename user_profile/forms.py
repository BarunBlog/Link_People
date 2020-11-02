from django import forms

from .models import UserProfileInfo

class DateInput(forms.DateInput):
    input_type = 'date'

class SaveProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ['User_image', 'Headline', 'Current_position', 'Summary', 'School_or_College_or_University',
        'Degree', 'Field_of_study', 'Education_Start_year', 'Education_End_year', 'Experience_Title', 'Employee_type',
        'Company', 'Start_year', 'End_year', 'Skill']

        widgets = {
            'Education_Start_year': DateInput(),
            'Education_End_year': DateInput(),
            'Start_year': DateInput(),
            'End_year': DateInput(),

        }
    
    '''def __init__(self, *args, **kwargs):
        super(SaveProfileForm, self).__init__(*args, **kwargs)
        self.fields['User_image'].required = False'''