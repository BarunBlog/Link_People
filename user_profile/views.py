from django.views.generic import DetailView

from .models import UserProfileInfo
from users.models import CustomUser

from django.shortcuts import redirect, render

from .forms import SaveProfileForm

#class DetailUserProfileInfo(DetailView):
def DetailUserProfileInfo(request, pk):
    """model = UserProfileInfo
    #context_object_name = 'UserProfile'
    template_name = 'user_profile/user_profile.html'''

    '''def get_queryset(self):
        return UserProfileInfo.objects.select_related('id')'''

    def get_context_data(self, **kwargs):
        context = super(DetailUserProfileInfo, self).get_context_data(**kwargs)
        context['custom_user'] = CustomUser.objects.filter(id=self.request.user.id)[0]
        '''a = UserProfileInfo.objects.filter(id_id=self.request.user.id)[0]
        if not a:
            context['message'] = 'Profile not updated'
        else:
            context['user_profile_info'] = a
            context['message'] = 'Profile updated'''
        
        return context"""

    custom_user = CustomUser.objects.filter(id=request.user.id)[0]
    a = UserProfileInfo.objects.filter(id_id=request.user.id)
    user_profile_info = None
    if not a:
        message = 'Profile not updated'
    else:
        user_profile_info = a[0]
        message = 'Profile updated'
    

    if request.method == "POST":
        form = SaveProfileForm(request.POST)
        if form.is_valid():
            
            User_image = form.cleaned_data['User_image']
            Headline = form.cleaned_data['Headline']
            Current_position = form.cleaned_data['Current_position']
            Summary = form.cleaned_data['Summary']
            School_or_College_or_University = form.cleaned_data['School_or_College_or_University']
            Degree = form.cleaned_data['Degree']
            Field_of_study = form.cleaned_data['Field_of_study']
            Education_Start_year = form.cleaned_data['Education_Start_year']
            Education_End_year = form.cleaned_data['Education_End_year']
            Experience_Title = form.cleaned_data['Experience_Title']
            Employee_type = form.cleaned_data['Employee_type']
            Company = form.cleaned_data['Company']
            Start_year = form.cleaned_data['Start_year']
            End_year = form.cleaned_data['End_year']
            Skill = form.cleaned_data['Skill']
            id_id = request.user.id

            p = UserProfileInfo.objects.create(User_image=User_image, Headline=Headline, Current_position=Current_position, Summary=Summary,
                School_or_College_or_University=School_or_College_or_University, Degree=Degree, Field_of_study=Field_of_study,
                Education_Start_year=Education_Start_year, Education_End_year=Education_End_year,
                Experience_Title=Experience_Title, Employee_type=Employee_type, Company=Company, Start_year=Start_year,
                End_year=End_year, Skill=Skill, id_id=id_id)
            
            p.save()
            
            
           
            return redirect('user_profile_info', pk=p.pk)

        else:
            print(form.errors)
            message = form.errors
            return render(request, "message/error.html", {'message': message})
    else:
        form = SaveProfileForm()

    
    
    return render(request, 'user_profile/user_profile.html', {'custom_user': custom_user, 'message': message,
            'user_profile_info':user_profile_info, 'form':form})
    
    



def GetUserProfileUuId(request):
    profile_uuid = UserProfileInfo.objects.filter(id_id=request.user.id).values('u_id')

    if not profile_uuid:
        user_uuid = CustomUser.objects.filter(id=request.user.id).values('uuid')
        return redirect('user_profile_info', user_uuid[0]["uuid"])
    else:
        return redirect('user_profile_info', profile_uuid[0]["u_id"])





'''def DetailUserProfileInfo(request, id):

    data = UserProfileInfo.objects.get(u_id=id)
    return render(request, 'user_profile/user_profile.html', {'UserProfile': data})'''
