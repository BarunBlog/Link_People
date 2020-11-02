from django.contrib.auth import get_user_model
from django.test import TestCase #an extension of Python’s TestCase

from django.urls import reverse, resolve

from .models import (
    PostJobModel,
    ApplicationModel
)

from .views import (
    createJobView,
    JobListView,
    JobsDetailView,
    SearchResultsListView,
    applicantCreateView,
    ApplicantList,
)  

#from .forms import 


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='partho',
            email='partho007@gmail.com',
            password='testpass123',
            first_name='Partho',
            last_name='Bhattacharjee',
            country='Bangladesh',
            city_or_district='Sylhet'
        )

        self.assertEqual(user.email, 'partho007@gmail.com')
        self.assertEqual(user.country, 'Bangladesh')
        self.assertEqual(user.city_or_district, 'Sylhet')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )


        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class JobsTests(TestCase): # new
    def setUp(self):
        url = reverse('job_list')
        self.response = self.client.get(url)

        self.client.login(email='partho007@gmail.com', password='testpass123')



    def test_job_post(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='partho',
            email='partho007@gmail.com',
            password='testpass123',
            first_name='Partho',
            last_name='Bhattacharjee',
            country='Bangladesh',
            city_or_district='Sylhet'
        )
        post = PostJobModel.objects.create(
            Job_author_id=user.id,
            Job_title='Sales Executive',
            Company='Unique Trading Company',
            Job_location='Dhaka, Bangladesh',
            Employee_type='Full-time',
            Description='szdfg lzsiuUS DhfkSJDHfiuSHDfLIDbfgysDgfbKSDGfiAeir AfIUGDlsf.',
            Add_skills='aroshA OgoSHDfguHAS DfiDHfiADF'
        )

        self.assertEqual(post.Job_title, 'Sales Executive')
        self.assertEqual(post.Company, 'Unique Trading Company')
        self.assertEqual(post.Job_location, 'Dhaka, Bangladesh')
        self.assertTrue(post.Employee_type, 'Full-time')
        self.assertTrue(post.Description, 'szdfg lzsiuUS DhfkSJDHfiuSHDfLIDbfgysDgfbKSDGfiAeir AfIUGDlsf.')
        self.assertTrue(post.Add_skills, 'aroshA OgoSHDfguHAS DfiDHfiADF')
        self.assertFalse(post.Is_approved, 'True')


    def test_job_list_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'jobs/job_list.html')
        self.assertContains(self.response, 'Search for your next job')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def job_detail_view(self):

        post = PostJobModel.objects.create(
            Job_title='Sales Executive',
            Company='Unique Trading Company',
            Job_location='Dhaka, Bangladesh',
            Employee_type='Full-time',
            Description='szdfg lzsiuUS DhfkSJDHfiuSHDfLIDbfgysDgfbKSDGfiAeir AfIUGDlsf.',
            Add_skills='aroshA OgoSHDfguHAS DfiDHfiADF'
        )

        response = self.client.get(post.get_absolute_url())
        no_response = self.client.get('/jobs/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Sales Executive')
        self.assertTemplateUsed(response, 'jobs/job_detail.html')