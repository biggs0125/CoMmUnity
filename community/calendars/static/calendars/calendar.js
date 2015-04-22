$(document).ready(function() {
    $('#calendar').fullCalendar({
	events: {
            url: 'http://localhost:8000/api/event/retrieve',
            type: 'GET',
	    success: function(events) {
		for (var i=0;i<events.length;i++) {
		    events[i] = events[i]['fields'];
		    events[i]['start'] = events[i]['start_datetime'];
		    events[i]['end'] = events[i]['end_datetime'];
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
	    $(element).tooltip({
		html: true,
		title: "Description: "+event['description']+"<br>"+"Start: "+moment(event['start']).format("LL h:MM")+"<br>"+"End: "+moment(event['end']).format("LL h:MM"),
		trigger: 'hover'
	    });
	},
	header: {
	    left: 'title',
	    center: '',
	    right: 'today prev,next month,agendaWeek,agendaDay'
	}
    })
});
