from django.shortcuts import render
from django.views.generic.base import TemplateView

class CreateEvent(TemplateView):
      template_name = 'calendars.html'
