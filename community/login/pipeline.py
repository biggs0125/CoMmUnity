from django.http import HttpResponseRedirect
from users.models import OurUser

def handle_info(request, details, response, *args, **kwargs):
    request.session['user_info'] = {'username' : details['username'],
                                    'name' : response['name']} 
    del request.session['partial_pipeline']
    request.session.save()
