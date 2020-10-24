from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView

from .models import PostJobModel
from .forms import PostJobForm

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.db.models import Q


class CreateJobView(LoginRequiredMixin, CreateView):
    form_class = PostJobForm
    template_name = 'jobs/post_job.html'
    success_message = 'Your job post is waiting for approval'
    success_url = reverse_lazy('job_list')
    login_url = 'account_login'



class JobListView(ListView):
    model = PostJobModel
    context_object_name = 'job_list'
    template_name = 'jobs/job_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        a = PostJobModel.objects.filter(Is_approved=True)
        
        context['job_list'] = a

        
        return context



class JobsDetailView(LoginRequiredMixin, DetailView):
    model = PostJobModel
    context_object_name = 'job_detail'
    template_name = 'jobs/job_detail.html'



class SearchResultsListView(ListView):
    model = PostJobModel
    context_object_name = 'search_job_list'
    template_name = 'jobs/search_results.html'
    #queryset = PostJobModel.objects.filter(Job_title__icontains='executive')

    def get_queryset(self):
        query1 = self.request.GET.get('q1')
        query2 = self.request.GET.get('q2')

        return PostJobModel.objects.filter(
            (Q(Job_title__icontains=query1) | Q(Add_skills__icontains=query1) | Q(Company__icontains=query1))
            &
            Q(Job_location__icontains=query2)
        )

