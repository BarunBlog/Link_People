from django.urls import path

from .views import JobListView, createJobView, JobsDetailView, SearchResultsListView

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<uuid:pk>', JobsDetailView.as_view(), name='jobs_details'),
    path('post-job/', createJobView, name='post_job'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    
]