from django.urls import path

from .views import DetailUserProfileInfo, GetUserProfileUuId

urlpatterns = [
    path('id/', GetUserProfileUuId, name='get_user_model_id'),
    #path('<uuid:pk>', DetailUserProfileInfo, name='user_profile_info'),
    path('<uuid:pk>', DetailUserProfileInfo.as_view(), name='user_profile_info'),
]