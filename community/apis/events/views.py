from django.views.generic import View
from events.models import Event
from tags.models import Tag
from users.models import OurUser
from datetime import datetime
from django.core import serializers
from organizations.models import Organization
from django.core.exceptions import ObjectDoesNotExist
from apis.CORSHttp import CORSHttpResponse
from slugify import slugify
from django.http import JsonResponse

class CreateEvent(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        self.creator = request.POST['creator']
        self.name = request.POST['name']
        self.start_date = request.POST['start_date']
        self.start_time = request.POST['start_time']
        self.end_date = request.POST['end_date']
        self.end_time = request.POST['end_time']
        self.location = request.POST['location']
        self.organization = request.POST['host']
        self.description = request.POST['description']
        self.tags = request.POST.getlist('tag')

        try:
            org = Organization.objects.get(name=self.organization)
        except ObjectDoesNotExist:
            return CORSHttpResponse(status=400)

        access_granted = False
        for admin in org.admins.all():
            if self.creator == admin.username:
                access_granted = True

        if not access_granted:
            return CORSHttpResponse(status=400)

        try:
            org = Organization.objects.get(name=self.organization)
            org_tag = org.org_tag
        except ObjectDoesNotExist:
            return CORSHttpResponse(status=500)

        try:
            start_date_obj = datetime.strptime(self.start_date, '%Y-%m-%d')
            start_time_obj = datetime.strptime(self.start_time, '%H:%M')
            end_date_obj = datetime.strptime(self.end_date, '%Y-%m-%d')
            end_time_obj = datetime.strptime(self.end_time, '%H:%M')
        except ValueError:
            return CORSHttpResponse(status=400)


        tags_list = [Tag.objects.get_or_create(name=slugify(tag, separator="_"))[0] for tag in self.tags]
        tags_list.append(org_tag)

        hosts_list = [org]

        start_datetime_obj = datetime.combine(start_date_obj.date(), start_time_obj.time())
        end_datetime_obj = datetime.combine(end_date_obj.date(), end_time_obj.time())

        if end_datetime_obj < start_datetime_obj:
            return CORSHttpResponse(status=400)

        event = Event(name=self.name, start_datetime=start_datetime_obj, end_datetime=end_datetime_obj,
                      description=self.description, location=self.location)
        event.save()
        event.tags = tags_list
        event.hosts = hosts_list
        event.attendees = list(org.admins.all())
        event.save()
        return CORSHttpResponse(status=200)

class GetEvent(View):

    def handle_id(self, event_id):
        return [Event.objects.get(pk=event_id)]

    def handle_date_range(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date+" 23:59:59", '%Y-%m-%d %H:%M:%S')
        return Event.objects.filter(start_datetime__gte=start_date, start_datetime__lte=end_date)

    def handle_date(self, event_date):
        return self.handle_date_range(event_date, event_date)

    def handle_tags(self, tags):
        return Event.objects.filter(tags__name__in=tags).distinct()

    def handle_params(self, qdict):

        if 'id' in qdict:
            return self.handle_id(qdict['id'])

        if 'date' in qdict:
            try:
                return self.handle_date(qdict['date'])
            except ValueError:
                return None

        if 'start_date' in qdict and 'end_date' in qdict:
            try:
                return self.handle_date_range(qdict['start_date'], qdict['end_date'])
            except ValueError:
                return None

        if 'tag' in qdict:
            return self.handle_tags(qdict.getlist('tag'))
            
        return None

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)

        events = self.handle_params(request.GET)

        attending = []
        not_attending = []

        if 'username' in request.GET:
            try:
                user = OurUser.objects.get(username=request.GET['username'])
                for e in events:
                    if user in e.attendees.all():
                        attending.append(e)
                    else:
                        not_attending.append(e)
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=404)
        else:
            not_attending = events

        if events is None:
            return CORSHttpResponse(status=400)
        
        serialized_attending = serializers.serialize("json", attending)
        serialized_not_attending = serializers.serialize("json", not_attending)
        json = JsonResponse({'attending': serialized_attending, 'not_attending': serialized_not_attending}, safe=False)
        return CORSHttpResponse(status=200, content=json, content_type="application/json")

class AddAttendee(View):
    
    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        if 'event' in request.POST.keys() and 'username' in request.POST.keys():
            try:
                user = OurUser.objects.get(username=request.POST['username'])
                event = Event.objects.get(pk=request.POST['event'])
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=404)
        else:
            return CORSHttpResponse(status=400)

        event.attendees.add(user)
        event.save()
        return CORSHttpResponse(status=200)

class SubscribedEvents(View):
    
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
        
        tags = [tag.name for tag in user.subscriptions.all()]
        events = []

        for e in Event.objects.all():
            for tag in e.tags.all():
                if tag.name in tags:
                   events.append(e)
                   break
        
        serialized_event = serializers.serialize("json", events)
        return CORSHttpResponse(status=200, content=serialized_event, content_type="application/json")

class UnattendEvent(View):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.method == 'POST':
            return CORSHttpResponse(status=403)
    
        if 'username' in request.POST.keys() and 'event' in request.POST.keys():
            try:
                user = OurUser.objects.get(username=request.POST['username'])
                event = Event.objects.get(pk=request.POST['event'])
                event.attendees.remove(user)
                event.save()
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=404)
        else:
            return CORSHttpResponse(status=400)

        return CORSHttpResponse(status=200)
