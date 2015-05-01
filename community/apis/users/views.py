from django.views.generic import View
from users.models import OurUser
from tags.models import Tag
from events.models import Event
from django.core import serializers
from apis.CORSHttp import CORSHttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from slugify import slugify
from datetime import datetime
class GetUser(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        if 'username' in request.POST:
            username = request.POST['username']
            user_obj, created = OurUser.objects.get_or_create(username=username)

            json_response = JsonResponse({"new" : created})
            return CORSHttpResponse(status=200, content=json_response.content, content_type="application/json")


class AddSubscriptions(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=404)

        if 'username' in request.POST:
            self.username = request.POST['username']
        else:
            return CORSHttpResponse(status=400)
            
        self.tags = request.POST.getlist('tag')

        try:
            user = OurUser.objects.get(username=self.username)
        except ObjectDoesNotExist:
            return CORSHttpResponse(status=403)

        tag_objs = []
        for tag in self.tags:
            try:
                tag_objs.append(Tag.objects.get(name=slugify(tag, separator="_")))
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=404)

        for tag in tag_objs:
            user.subscriptions.add(tag)

        user.save()

        return CORSHttpResponse(status=200)


class GetSubscriptions(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)
        
        if 'username' in request.GET.keys():
            self.username = request.GET['username']
        else:
           return CORSHttpResponse(status=400) 

        try:
            user = OurUser.objects.get(username=self.username)
        except ObjectDoesNotExist:
            return CORSHttpResponse(status=404)

        subs = [tag.name for tag in user.subscriptions.all()]
        serialized_response = JsonResponse({"tags": subs}, safe=False)
        return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")

class GetAttending(View):
    
    def dispatch(self, request, *args, **kwargs):
    
        if not request.method == 'GET':
            return CORSHttpResponse(status=403)
        
        if 'username' in request.GET.keys():
            try:
                user = OurUser.objects.get(username=request.GET['username'])
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=404)
        else:
            return CORSHttpResponse(status=400)
        events = Event.objects.filter(attendees__id__exact=user.pk, end_datetime__gt=datetime.now())
        serialized_response = serializers.serialize("json", events)

        return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")
