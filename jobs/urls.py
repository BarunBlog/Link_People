from django.urls import path

from .views import JobListView, CreateJobView, JobsDetailView

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<uuid:pk>', JobsDetailView.as_view(), name='jobs_details'),
    path('post-job/', CreateJobView.as_view(), name='post_job')
    #path('<uuid:pk>', detailUserProfileInfo, name='user_profile_info'),
    #path('<uuid:pk>', updateUserProfileInfo, name='update_user_profile_info'),
]