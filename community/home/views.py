from django.views.generic.base import TemplateView
from django.contrib.sessions.models import Session

class CreateEvent(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        return super(CreateEvent, self).dispatch(request, *args, **kwargs)
