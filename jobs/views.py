import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import PostJobModel, ApplicationModel
from user_profile.models import UserProfileInfo
from users.models import CustomUser
from .forms import PostJobForm

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy

from django.db.models import Q

from django.shortcuts import render, redirect, HttpResponseRedirect, reverse



@login_required
def createJobView(request):
    if request.method == "POST":
        form = PostJobForm(request.POST)
        if form.is_valid():

            Job_title = form.cleaned_data['Job_title']
            Company = form.cleaned_data['Company']
            Job_location = form.cleaned_data['Job_location']
            Employee_type = form.cleaned_data['Employee_type']
            Description = form.cleaned_data['Description']
            Add_skills = form.cleaned_data['Add_skills']
            

            p = PostJobModel.objects.create(Job_title=Job_title, Company=Company, 
            Job_location=Job_location, Employee_type=Employee_type, Description=Description,
            Add_skills=Add_skills, Job_author_id=request.user.id)
            
            p.save()

            CustomUser.objects.filter(id=request.user.id).update(is_posted_job=True)
            
           
            return redirect('onlyRedirect')

        else:
            print(form.errors)
            message = form.errors
            return render(request, "message/error.html", {'message': message})
    
    else:
        form = PostJobForm()
    
    return render(request, 'jobs/post_job.html', {'form':form})


def onlyRedirect(request):
    message = 'Your job post is waiting for approval'
    job_list = PostJobModel.objects.filter(Is_approved=True)

    return render(request, 'jobs/job_list.html', {'message': message, 'job_list': job_list})


class JobListView(ListView):
    model = PostJobModel
    context_object_name = 'job_list'
    template_name = 'jobs/job_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['job_list'] = PostJobModel.objects.filter(Is_approved=True)

        if self.request.user.id:
            context['is_posted_job'] = CustomUser.objects.filter(id=self.request.user.id).values('is_posted_job')[0]["is_posted_job"]
            

        
        return context



class JobsDetailView(LoginRequiredMixin, DetailView):
    model = PostJobModel
    context_object_name = 'job_detail'
    template_name = 'jobs/job_detail.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        b = UserProfileInfo.objects.filter(id_id=self.request.user.id)

        if b:
            context['is_user_profile_created'] = True
        else:
            context['is_user_profile_created'] = False

    
        return context



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

    a = ApplicationModel.objects.filter(Applicant_id=request.user.id, Job_id=Job_id)

    if a.exists():
        return render(request, 'jobs/already_applied.html', {'message': 'You have already applied to this post.'})

    else:
        p = ApplicationModel.objects.create(Job_id=Job_id, Job_title=Job_title, 
            Applicant_id=Applicant_id, first_name=request.user.first_name, last_name=request.user.last_name)

        p.save()

        return redirect('application_done')



class ApplicationDone(TemplateView):
    template_name = 'jobs/application_done.html'



class ApplicantList(LoginRequiredMixin, ListView):
    model = ApplicationModel
    context_object_name = 'applicant_list'
    template_name = 'jobs/applicant_list.html'

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)


        context['applicant_list'] = ApplicationModel.objects.filter(Job__Job_author_id=self.request.user.id)

                
        return context