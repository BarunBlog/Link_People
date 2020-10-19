from django.views.generic import DetailView

from .models import UserProfileInfo
from users.models import CustomUser

from django.shortcuts import redirect, render

class DetailUserProfileInfo(DetailView):
    model = UserProfileInfo
    context_object_name = 'UserProfile'
    template_name = 'user_profile/user_profile.html'

    def get_queryset(self):
        return UserProfileInfo.objects.filter(id_id=self.request.user.id).select_related()


def GetUserProfileUuId(request):
    uuid = UserProfileInfo.objects.filter(id_id=request.user.id).values('u_id')
    return redirect('user_profile_info', uuid[0]["u_id"])


'''def DetailUserProfileInfo(request, id):

    data = UserProfileInfo.objects.get(u_id=id)
    return render(request, 'user_profile/user_profile.html', {'UserProfile': data})'''
