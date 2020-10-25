from django.urls import path

from .views import (
    BlogListView,
    SearchResultsListView,
    BlogDetailView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<uuid:pk>', BlogDetailView.as_view(), name='blog_details'),
    path('search/', SearchResultsListView.as_view(), name='blog_search_results'),
    
]