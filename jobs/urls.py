from django.urls import path

from .views import (
    JobListView, 
    createJobView, 
    JobsDetailView, 
    SearchResultsListView, 
    applicantCreateView,
    ApplicantList,
    onlyRedirect,
    ApplicationDone,
)

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<uuid:pk>', JobsDetailView.as_view(), name='jobs_details'),
    path('post-job/', createJobView, name='post_job'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('apply/', applicantCreateView, name='apply_job'),
    path('apply-done/', ApplicationDone.as_view(), name='application_done'),
    path('applicant-list/', ApplicantList.as_view(), name='applicant_list'),
    path('only-redirect/', onlyRedirect, name='onlyRedirect')
    
]