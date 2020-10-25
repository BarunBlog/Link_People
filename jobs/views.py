import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView

from .models import PostJobModel, ApplicationModel
from users.models import CustomUser
from .forms import PostJobForm

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy

from django.db.models import Q

from django.shortcuts import render, redirect, HttpResponseRedirect, reverse


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
            

            p = PostJobModel.objects.create(Job_title=Job_title, Company=Company, 
            Job_location=Job_location, Employee_type=Employee_type, Description=Description,
            Add_skills=Add_skills)
            
            p.save()

            CustomUser.objects.filter(id=request.user.id).update(is_posted_job=True)
            
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
        context['is_posted_job'] = CustomUser.objects.filter(id=self.request.user.id).values('is_posted_job')[0]["is_posted_job"]
        
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

@login_required
def applicantCreateView(request):
    Job_id = uuid.UUID(request.POST.get('id'))
    Job_title = PostJobModel.objects.filter(Job_id=Job_id)[0].Job_title
    Applicant_id = request.user.id

    p = ApplicationModel.objects.create(Job_id=Job_id, Job_title=Job_title, 
            Applicant_id=Applicant_id)
            
    p.save()

    message = 'You have successfully applied'
      
           
    #return HttpResponseRedirect(reverse('jobs_details', args={Job_id}), {'message':message})

    return render(request, 'jobs/application_done.html', {'message':message})



class ApplicantList(LoginRequiredMixin, ListView):
    model = ApplicationModel
    context_object_name = 'applicant_list'
    template_name = 'jobs/applicant_list.html'

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        context['first_name'] = CustomUser.objects.filter(id=self.request.user.id).values('first_name')[0]["first_name"]
        context['last_name'] = CustomUser.objects.filter(id=self.request.user.id).values('last_name')[0]["last_name"]
        
        return context