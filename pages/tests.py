from django.test import SimpleTestCase 
#which is a special subset of Django’s TestCase that is designed for webpages that do not have a model included.

from django.urls import reverse, resolve
#which is useful for testing our URLs.
from .views import HomePageView, AboutPageView



class HomepageTests(SimpleTestCase):
    '''
    The two tests here both check that the HTTP status code for the homepage equals
    200 which means that it exists.
    '''

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url) # accesses the homepage (/)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200) #Python’s assertEqual to check that the status code matches 200.


    '''
    We’ve created a response variable again and then checked that the template home.html
    is used.
    '''
    def test_homepage_template(self):

        self.assertTemplateUsed(self.response, 'home.html')

    '''
    Let’s now confirm that our homepage has the correct HTML code and also does not
    have incorrect text.
    '''

    def test_homepage_contains_correct_html(self):

        self.assertContains(self.response, 'Jobs')

    def test_homepage_does_not_contains_incorrect_html(self):

        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
    '''
    A final views check we can do is that our HomePageView “resolves” a given URL path.
    checks that the name of the view used to resolve / matches HomePageView.
    '''
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About LinkPeople')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )
    
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )