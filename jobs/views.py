from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView

from .models import PostJobModel
from .forms import PostJobForm

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy

from django.db.models import Q

from django.shortcuts import render, redirect


'''class CreateJobView(LoginRequiredMixin, CreateView):
    form_class = PostJobForm
    template_name = 'jobs/post_job.html'
    success_message = 'Your job post is waiting for approval'
    success_url = reverse_lazy('job_list')
    login_url = 'account_login'
    messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')'''

@login_required
def createJobView(request):
    if request.method == "POST":
        form = PostJobForm(request.POST)
        if form.is_valid():
        
            job_list = PostJobModel.objects.filter(Is_approved=True)

            Job_title = form.cleaned_data['Job_title']
            Company = form.cleaned_data['Company']
            Job_location = form.cleaned_data['Job_location']
            Employee_type = form.cleaned_data['Employee_type']
            Description = form.cleaned_data['Description']
            Add_skills = form.cleaned_data['Add_skills']
            Email_address = form.cleaned_data['Email_address']
            

            p = PostJobModel.objects.create(Job_title=Job_title, Company=Company, 
            Job_location=Job_location, Employee_type=Employee_type, Description=Description,
            Add_skills=Add_skills, Email_address=Email_address)
            
            p.save()
            
            message = 'Your job post is waiting for approval'
            
           
            return render(request, 'jobs/job_list.html', {'message': message, 'job_list':job_list})

        else:
            print(form.errors)
            message = form.errors
            return render(request, "message/error.html", {'message': message, 'job_list':job_list})
    
    else:
        form = PostJobForm()
    
    return render(request, 'jobs/post_job.html', {'form':form})



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
            &
            Q(Is_approved__icontains=True)
        )

