$(document).ready(function() {
    $('#calendar').fullCalendar({
	events: {
            url: 'http://localhost:8000/api/event/retrieve',
            type: 'GET',
	    success: function(events) {
		for (var i=0;i<events.length;i++) {
		    events[i] = events[i]['fields'];
		    events[i]['start'] = events[i]['datetime'];
		}
	    },
            error: function() {
		alert('there was an error while fetching events!');
            },
            textColor: 'black', // a non-ajax option
	    startParam: 'start_date',
	    endParam: 'end_date'
	},
	eventRender: function(event, element) {
	    $(element).append(event['name']);
	    $(element).hover(function() {
		
	    });
	},
	header: {
	    left: 'title',
	    center: '',
	    right: 'today prev,next month,agendaWeek,agendaDay'
	}
    })
});
