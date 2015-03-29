from django.shortcuts import render
from django.views.generic import View
from events.models import Event
from datetime import datetime, time, date

class CreateEvent(View):

    def dispatch(self, request, *args, **kwargs):

        if not request['method'] == 'POST':
            pass

        self.name = request['name']
        self.date = request['date']
        self.time = request['time']
        self.location = request['location']
        self.description = request['description']
        
        date_obj = date.strptime(self.date, '%m-%d-%Y')
        time_obj = time.strptime(self.time, '%H:%M')
        datetime_obj = datetime.combine(date_obj, time_obj)
        event = Event(name=self.name, datetime=datetime_obj, description=self.description,
                location=self.location)

        event.save()

