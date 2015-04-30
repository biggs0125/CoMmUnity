from django.views.generic.base import TemplateView
from django.shortcuts import redirect

class CreateEvent(TemplateView):
    template_name = 'create_event.html'

    def dispatch(self, request, *args, **kwargs):
        if not 'user' in request.session.keys():
            return redirect('home')
        else:
            return super(CreateEvent, self).dispatch(request, *args, **kwargs)
        
