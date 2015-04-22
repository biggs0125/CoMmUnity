from django.views.generic import View
from events.models import Event
from tags.models import Tag
from datetime import datetime
from django.core import serializers
from apis.CORSHttp import CORSHttpResponse


class CreateEvent(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        self.name = request.POST['name']
        self.start_date = request.POST['start_date']
        self.start_time = request.POST['start_time']
        self.end_date = request.POST['end_date']
        self.end_time = request.POST['end_time']
        self.location = request.POST['location']
        self.description = request.POST['description']
        self.tags = request.POST.getlist('tag')

        try:
            start_date_obj = datetime.strptime(self.start_date, '%Y-%m-%d')
            start_time_obj = datetime.strptime(self.start_time, '%H:%M')
            end_date_obj = datetime.strptime(self.end_date, '%Y-%m-%d')
            end_time_obj = datetime.strptime(self.end_time, '%H:%M')
        except ValueError:
            return CORSHttpResponse(status=400)


        tags_list = [Tag.objects.get_or_create(name=tag)[0] for tag in self.tags]

        start_datetime_obj = datetime.combine(start_date_obj.date(), start_time_obj.time())
        end_datetime_obj = datetime.combine(end_date_obj.date(), end_time_obj.time())

        event = Event(name=self.name, start_datetime=start_datetime_obj, end_datetime=end_datetime_obj,
                      description=self.description, location=self.location)

        event.save()
        event.tags = tags_list
        event.save()
        return CORSHttpResponse(status=200)

class GetEvent(View):

    def handle_id(self, event_id):
        return [Event.objects.get(pk=event_id)]

    def handle_date_range(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date+" 23:59:59", '%Y-%m-%d %H:%M:%S')
        return Event.objects.filter(datetime__gte=start_date, datetime__lte=end_date)

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

        event = self.handle_params(request.GET)

        if event is None:
            return CORSHttpResponse(status=400)

        serialized_event = serializers.serialize("json", event)
        return CORSHttpResponse(status=200, content=serialized_event, content_type="application/json")
