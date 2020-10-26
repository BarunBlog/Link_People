'''from django.contrib.auth import get_user_model
from django.test import TestCase #an extension of Python’s TestCase

from django.urls import reverse, resolve

from django.test import Client

from .models import PremiumBlog

from .views import (
    BlogListView,
    BlogDetailView,
)  



class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='partho',
            email='partho007@gmail.com',
            first_name='Partho',
            last_name='Bhattacharjee',
            country='Bangladesh',
            city_or_district='Sylhet'
        )
        user.set_password('testpass123')
        user.save()

        self.assertEqual(user.email, 'partho007@gmail.com')
        self.assertEqual(user.country, 'Bangladesh')
        self.assertEqual(user.city_or_district, 'Sylhet')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


class BlogTests(TestCase):
    def setUp(self):
        c = Client()
        c.login(email='partho007@gmail.com', password='testpass123')

        url = reverse('blog_list')
        self.response = self.client.get(url)




    def test_job_post(self):
        post = PremiumBlog.objects.create(
            Author='Barun',
            Title='What is Django?',
            Description='Python Framework',
        )

        self.assertEqual(post.Author, 'Barun')
        self.assertEqual(post.Title, 'What is Django?')
        self.assertEqual(post.Description, 'Python Framework')


    def test_job_list_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'premium/blog_list.html')
        self.assertContains(self.response, 'Search your blog here')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def job_detail_view(self):

        post = PremiumBlog.objects.create(
            Author='Barun',
            Title='What is Django?',
            Description='Python Framework',
        )

        response = self.client.get(post.get_absolute_url())
        no_response = self.client.get('/jobs/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'What is Django?')
        self.assertTemplateUsed(response, 'premium/blog_detail.html')'''