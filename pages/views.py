from django.shortcuts import render
from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name='home.html'

class Movies_cat(TemplateView):
    template_name='movies_catagories.html'

class Movies_list(TemplateView):
    template_name='movies_list.html'