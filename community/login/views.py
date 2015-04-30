from django.views.generic import RedirectView

class LogoutView(RedirectView):
    pattern_name = "home"
    permanent = False
    
    def dispatch(self, request, *args, **kwargs):
        session = request.session
        del session['user_info']
        session.save()
        return super(LogoutView, self).dispatch(request, *args, **kwargs)
