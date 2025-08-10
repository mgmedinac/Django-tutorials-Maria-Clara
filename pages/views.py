from django.shortcuts import render
from django.views.generic import TemplateView

class homePageView(TemplateView):
    template_name= 'pages/home.html'
    