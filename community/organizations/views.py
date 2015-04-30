from django.views.generic.base import TemplateView
from django.shortcuts import redirect
        
class CreateOrganization(TemplateView):
      template_name = 'create_organization.html'

      def dispatch(self, request, *args, **kwargs):
            if not 'user' in request.session.keys():
                  return redirect('home')
            else:
                  return super(CreateOrganization, self).dispatch(request, *args, **kwargs)

