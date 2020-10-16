from django.shortcuts import render
from django.views.generic import TemplateView

'''
We can leverage Django’s built-in TemplateView so
that the only tweak needed is to specify our desired template, home.html
'''
class HomePageView(TemplateView):
    template_name = 'home.html'