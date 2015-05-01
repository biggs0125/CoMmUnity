cur_filt = ''; // Global to hold the current filter

$(document).ready(function() {

    // Get the tag names via GET request and append them to
    // the description
    function getTagNames(event, desc, callback) {

        var tagIds = event['tags'];

        // If there are no tags, don't make a request to the server
        if (tagIds.length == 0) {
            desc += 'None';
            callback(event, desc, []);
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
                callback(event, desc, tagNames); 
            },
        });

    }

    // Print the event description that goes in the tooltip
    function printDesc(event, desc, callback) {
        desc = "Description: "+event['description']+"<br>"+
               "Start: "+moment(event['start']).format("LL h:mm")+"<br>"+
               "End: "+moment(event['end']).format("LL h:mm")+"<br>"+
               "Tags: ";
        getTagNames(event, desc, callback);
    }
    
    // Apply chosen
    $("#filter").chosen();

    // Get all the tags
    $.ajax({
        url: "http://localhost:8000/api/tag/retrieve",
        method: "GET",
        data: { },
        success: function (events) {
            for (var i = 0; i < events.length; i++) {
                var name = events[i]['fields']['name'];
                $("#filter").append("<option value='" + name
                  + "'>" + name + "</option>");
                $("#filter").trigger("chosen:updated");
            }
        },
    });

    // Render the calendar
    $('#calendar').fullCalendar({
	events: {
            url: 'http://localhost:8000/api/event/retrieve',
            type: 'GET',
	    success: function(events) {
		for (var i = 0; i < events.length; i++) {
		    var id = events[i]['pk'];
		    events[i] = events[i]['fields'];
		    events[i]['start'] = events[i]['start_datetime'];
		    events[i]['end'] = events[i]['end_datetime'];
		    events[i]['id'] = id;
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
            var desc;
            printDesc(event, desc, function(event, desc, tags) {
	        $(element).append(event['name']);
                $(element).attr('tag', '');
                $(element).attr('event_id', event['id']);
                var tagFound = false;
                for (var i = 0; i < tags.length; i++) {

                    // Add tag attribute to element so we can reference tags later
                    // for filtering
                    $(element).attr('tag', $(element).attr('tag') + tags[i]['fields']['name'] + ' ');

                    // Search for tags matching the current filter
                    if (tags[i]['fields']['name'] == cur_filt || cur_filt == '') {
                        tagFound = true;
                    }
                }

                // Hide an event if it has no tags or is not
                // the current tag
                if (!tagFound && (tags.length != 0 || cur_filt != '')) {
                    $(element).hide();
                }

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
	},

	height: "auto",
	
	eventClick: function(calEvent, jsEvent, view) {
	    if(confirm("Are you attending?")) {
		$.ajax({
		    method: 'POST',
		    url: "http://localhost:8000/api/event/add_attendee",
		    data: {username: USERNAME,
			   event: calEvent['id']},
		    error: function() {
			alert("There was a problem confirming your attendance, please try again later.");
		    }
		});
	    }
	}
    })

    $("#filter_button").click(function() {
	var filt = $("#filter").val();
        cur_filt = filt;
        $(".fc-event").hide(); // Hide all
        $.each($(".fc-event"), function(i, x) {
            if ($(x).attr('tag').split(' ').indexOf(filt) >= 0) {
                $(x).show(); // Show just the ones with the tags
            }
        });
    });
});
