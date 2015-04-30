from django.http import HttpResponseRedirect
from users.models import OurUser

def handle_info(request, details, response, *args, **kwargs):
    request.session['user'] = OurUser.objects.get(username=details['username'])
    del request.session['partial_pipeline']
    request.session.save()
