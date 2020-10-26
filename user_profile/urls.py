from django.urls import path

from .views import (
    detailUserProfileInfo,
    GetUserProfileUuId,
    detailProfileViewForPublic,
    getUseridFromApplicantList
)

urlpatterns = [
    path('id/', GetUserProfileUuId, name='get_user_model_id'),
    path('<uuid:pk>', detailUserProfileInfo, name='user_profile_info'),
    path('uuid/', getUseridFromApplicantList, name='useridFromApplicantList'),
    path('public/<uuid:pk>', detailProfileViewForPublic, name='detailProfileViewForPublic'),
]