from django.views.generic.base import TemplateView
from django.shortcuts import redirect

class SubscribeView(TemplateView):
    template_name = 'subscribe.html'

    def dispatch(self, request, *args, **kwargs):
        if not 'user' in request.session.keys():
            return redirect('home')
        else:
            return super(SubscribeView, self).dispatch(request, *args, **kwargs)
