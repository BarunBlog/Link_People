import uuid
from django.views.generic import DetailView

from .models import UserProfileInfo
from users.models import CustomUser

from django.shortcuts import (
    redirect,
    render,
    get_object_or_404,
    HttpResponseRedirect,
    reverse
)

from .forms import SaveProfileForm



def detailUserProfileInfo(request, pk):

    """ Shows detailView of User"""


    a = UserProfileInfo.objects.filter(id_id=request.user.id)
    user_profile_info = None
    if not a:
        message = 'Profile not edited'
    else:
        user_profile_info = a[0]
        message = 'Profile edited'


    
    custom_user = CustomUser.objects.filter(id=request.user.id)[0]

    if request.method == "POST" and not a:
        form = SaveProfileForm(request.POST, request.FILES)
        if form.is_valid():
            
            User_image = form.cleaned_data['User_image']

            profile = form.save(commit=False)
            profile.first_name = request.user.first_name
            profile.last_name = request.user.last_name
            profile.id_id = request.user.id
            profile.save()
            

            if User_image:

                user_thumbnail = CustomUser.objects.get(id=request.user.id)
                user_thumbnail.image_thumbnail = User_image
                user_thumbnail.save()
            
            
           
            return redirect('user_profile_info', pk=profile.pk)

        else:
            print(form.errors)
            message = form.errors
            return render(request, "message/error.html", {'message': message})

    elif a:
        """ As Profile edited for the first time now when user click edit profile this 
        section of code will run and will update the data."""


        # fetch the object related to passed pk
        obj = get_object_or_404(UserProfileInfo, pk = pk)
        
        if request.method == "POST":
        
            # pass the object as instance in form 
            form = SaveProfileForm(request.POST, request.FILES, instance=obj) 
        
            # save the data from the form and 
            # redirect to detail_view 
            if form.is_valid(): 
                User_image = form.cleaned_data['User_image']

                profile = form.save(commit=False)
                profile.id_id = request.user.id
                profile.save()
                

                if User_image:

                    user_thumbnail = CustomUser.objects.get(id=request.user.id)
                    user_thumbnail.image_thumbnail = User_image
                    user_thumbnail.save()


                
                return redirect('user_profile_info', pk=pk) # Calling via url name
            else:
                print(form.errors)
                message = form.errors
                return render(request, "message/error.html", {'message': message})
        else:
            form = SaveProfileForm(instance=obj)
            #return render(request, "user_profile/user_profile.html", {'form':form})

    
    else:
        """As profile not edited yet for the first time so only going to render the form"""
        form = SaveProfileForm()

    
    
    return render(request, 'user_profile/user_profile.html', {'custom_user': custom_user, 'message': message,
            'user_profile_info':user_profile_info, 'form':form})



def getUseridFromApplicantList(request):
    Applicant_id = request.POST.get('id')
    #join_result = UserProfileInfo.objects.select_related('id')
    User_uuid = UserProfileInfo.objects.filter(id_id=Applicant_id).values('u_id')

    return redirect('detailProfileViewForPublic', User_uuid[0]["u_id"])


def detailProfileViewForPublic(request, pk):
    User_id = UserProfileInfo.objects.filter(u_id=pk).values('id_id')[0]["id_id"]
    join_result = UserProfileInfo.objects.filter(id_id=User_id).select_related()[0]

    return render(request, 'user_profile/user_profile_for_public.html', {'join_result': join_result})









def GetUserProfileUuId(request):
    profile_uuid = UserProfileInfo.objects.filter(id_id=request.user.id).values('u_id')

    if not profile_uuid:
        user_uuid = CustomUser.objects.filter(id=request.user.id).values('uuid')
        return redirect('user_profile_info', user_uuid[0]["uuid"])
    else:
        return redirect('user_profile_info', profile_uuid[0]["u_id"])


