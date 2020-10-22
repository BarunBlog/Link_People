'''from django.contrib.auth import get_user_model
from django.test import Client, TestCase #an extension of Python’s TestCase

from django.urls import reverse, resolve

from .models import UserProfileInfo
from .forms import SaveProfileForm
from .views import detailUserProfileInfo



class UserProfileTests(TestCase):


    def setup(self):
        
        self.client = Client()
            
        self.user = get_user_model().objects.create_user(
            username='partho00@gmail.com',
            email='partho01@gmail.com',
            password='testpass123',
            first_name='Partho',
            last_name='Bhattacharjee',
            country='Bangladesh',
            city_or_district='Sylhet',
        )

        self.client.login(email='partho007@gmail.com', password='testpass123')

        self.user_profile = UserProfileInfo.objects.create(
            User_image = 'profile_pic/test3_XL4JohJ.jpg',
            Headline = 'Python Developer',
            School_or_College_or_University = 'Metropolitan University',
            Degree = 'Bachelor of science',
            Field_of_study = 'Computer Science and Engineering',
            Education_Start_year = '2016-05-01',
            Education_End_year = '2020-05-01',
            id_id = self.user.id,
        )



    def test_user_profile(self):
        self.setup()
        self.assertEqual(f'{self.user_profile.User_image}', 'profile_pic/test3_XL4JohJ.jpg')
        self.assertEqual(f'{self.user_profile.Headline}', 'Python Developer')
        self.assertEqual(f'{self.user_profile.School_or_College_or_University}', 'Metropolitan University')
        self.assertEqual(f'{self.user_profile.Degree}', 'Bachelor of science')
        self.assertEqual(f'{self.user_profile.Field_of_study}', 'Computer Science and Engineering')
        self.assertEqual(f'{self.user_profile.Education_Start_year}', '2016-05-01')
        self.assertEqual(f'{self.user_profile.Education_End_year}', '2020-05-01')





    def test_user_profile_template(self):
        url = reverse('user_profile_info', args=(self.user_profile.u_id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/user_profile.html')
        self.assertContains(response, 'Education')
        self.assertNotContains(
        response, 'Hi there! I should not be on the page.')


    def test_user_profile_form(self):
        url = reverse('user_profile_info', args=(self.user_profile.u_id,))
        response = self.client.get(url)

        form = response.context.get('form')
        self.assertIsInstance(form, SaveProfileForm)
        self.assertContains(response, 'csrfmiddlewaretoken')


    def test_detailUserProfile_view(self):
        view = resolve('user_profile_info', args=(self.user_profile.u_id,))
        self.assertEqual(
            view.func.__name__,
            detailUserProfileInfo.__name__
        )'''