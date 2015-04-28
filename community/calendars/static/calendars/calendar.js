$(document).ready(function() {

    // Get the tag names via GET request and append them to
    // the description
    function getTagNames(event, desc, callback) {

        var tagIds = event['tags'];

        // If there are no tags, don't make a request to the server
        if (tagIds.length == 0) {
            desc += 'None';
            callback(event, desc);
            return;
        }

        // Send GET request
        jQuery.ajaxSettings.traditional = true;
        $.ajax({
            url: "http://localhost:8000/api/tag/retrieve",
            method: "GET",
            data: {
                id: tagIds
            },
            success: function (tagNames) {
                // Append the tag names to description
                for (var i = 0; i < tagNames.length-1; i++) {
                    desc += tagNames[i]['fields']['name'] + ", ";
                }
                desc += tagNames[tagNames.length-1]['fields']['name'];
                callback(event, desc); 
            },
            error: function() {
                //alert("Bad tag IDs");
            }
        });

    }

    // Print the event description that goes in the tooltip
    function printDesc(event, desc, callback) {
        desc = "Description: "+event['description']+"<br>"+
               "Start: "+moment(event['start']).format("LL h:MM")+"<br>"+
               "End: "+moment(event['end']).format("LL h:MM")+"<br>"+
               "Tags: ";
        getTagNames(event, desc, callback);
    }

    // Render the calendar
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
	    //console.log(event); 
            var desc;
            printDesc(event, desc, function(event, desc) {
	        $(element).append(event['name']);
	        $(element).tooltip({
		    html: true,
                    title: desc,
		    trigger: 'hover'
	        });
            });
	},
	header: {
	    left: 'title',
	    center: '',
	    right: 'today prev,next month,agendaWeek,agendaDay'
	}
    })
});
