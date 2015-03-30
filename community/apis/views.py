from django.shortcuts import render
from django.views.generic import View
from events.models import Event
from datetime import datetime, time, date
from django.http import HttpResponse

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

    def dispatch(self, request, id=None, *args, **kwargs):

        if not request.method == 'GET':
            return HttpResponse(status=403)

        event = Event.objects.get(pk=id)

        return HttpResponse(status=200)
