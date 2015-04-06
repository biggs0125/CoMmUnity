from django.shortcuts import render
from django.views.generic import View
from events.models import Event
from datetime import datetime, time, date
from django.http import HttpResponse
from django.core import serializers

class CreateEvent(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return HttpResponse(status=403)

        self.name = request.POST['name']
        self.date = request.POST['date']
        self.time = request.POST['time']
        self.location = request.POST['location']
        self.description = request.POST['description']
        
        date_obj = datetime.strptime(self.date, '%m-%d-%Y')
        time_obj = datetime.strptime(self.time, '%H:%M')
        datetime_obj = datetime.combine(date_obj.date(), time_obj.time())
        event = Event(name=self.name, datetime=datetime_obj, description=self.description,
                location=self.location)

        event.save()
        return HttpResponse(status=200)

class GetEvent(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return HttpResponse(status=403)

        print request.GET
        event = None
        if 'id' in request.GET:
            id = request.GET['id']
            event = [Event.objects.get(pk=id)]

        elif 'date' in request.GET:
            start_date = datetime.strptime(request.GET['date'], '%m-%d-%Y')
            end_date = datetime.strptime(request.GET['date']+" 23:59:59", '%m-%d-%Y %H:%M:%S')
            event = Event.objects.filter(datetime__gte=start_date, datetime__lte=end_date)

        elif 'start_date' in request.GET and 'end_date' in request.GET:
            start_date = datetime.strptime(request.GET['start_date'], '%m-%d-%Y')
            end_date = datetime.strptime(request.GET['end_date']+" 23:59:59", '%m-%d-%Y %H:%M:%S')
            event = Event.objects.filter(datetime__gte=start_date, datetime__lte=end_date)

        if event is None:
            return HttpResponse(status=400)

        serialized_event = serializers.serialize("json", event)
        return HttpResponse(status=200, content=serialized_event, content_type="application/json")
