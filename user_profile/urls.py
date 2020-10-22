from django.urls import path

from .views import detailUserProfileInfo, GetUserProfileUuId

urlpatterns = [
    path('id/', GetUserProfileUuId, name='get_user_model_id'),
    path('<uuid:pk>', detailUserProfileInfo, name='user_profile_info'),
    #path('<uuid:pk>', updateUserProfileInfo, name='update_user_profile_info'),
]