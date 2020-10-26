from django.shortcuts import render

from .models import PremiumBlog

from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from django.db.models import Q


class BlogListView(LoginRequiredMixin, ListView):
    model = PremiumBlog
    context_object_name = 'blog_list'
    template_name = 'premium/blog_list.html'



class BlogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = PremiumBlog
    context_object_name = 'blog_detail'
    template_name = 'premium/blog_detail.html'
    login_url = 'account_login'
    permission_required = 'get_premium.special_status' 



class SearchResultsListView(LoginRequiredMixin, ListView):
    model = PremiumBlog
    context_object_name = 'search_blog_list'
    template_name = 'premium/search_blog_list.html'
    #queryset = PostJobModel.objects.filter(Job_title__icontains='executive')

    def get_queryset(self):
        query1 = self.request.GET.get('q1')

        return PremiumBlog.objects.filter(
            Q(Title__icontains=query1)
        )
