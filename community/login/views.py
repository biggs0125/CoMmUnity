from django.views.generic import RedirectView
from django.contrib.auth import logout as auth_logout

class LogoutView(RedirectView):
    pattern_name = "home"
    permanent = False
    
    def dispatch(self, request, *args, **kwargs):
        session = request.session
        if 'user' in session.keys():
            del session['user']
            session.save()
        return super(LogoutView, self).dispatch(request, *args, **kwargs)
