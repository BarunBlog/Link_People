from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView

from .models import PostJobModel
from .forms import PostJobForm

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


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



class JobsDetailView(LoginRequiredMixin, DetailView):
    model = PostJobModel
    context_object_name = 'job_detail'
    template_name = 'jobs/job_detail.html'


