cur_filt = ''; // Global to hold the current filter

$(document).ready(function() {

    function handleAttend(event, element) {
	if(event.attending) {
	    if (typeof USERNAME != 'undefined') {
		$(element).find(".unattend").remove();
		var unat = $("<div class='unattend' event_id="+event['id']+"><span class='glyphicon glyphicon-remove' aria-hidden='true'></span><span>unattend?</span></div>");
		unat.click(function(e) {
		    var id = $(e.currentTarget).attr('event_id');
		    if(typeof USERNAME != 'undefined' && confirm("Cancel attendance?")) {
			$.ajax({
			    method: 'POST',
			    url: "http://localhost:8000/api/event/unattend",
			    data: {username: USERNAME,
				   event: id},
			    success: function() {
				window.location.pathname = "/calendar";
			    },
			    error: function() {
				alert("There was a problem confirming your attendance, please try again later.");
			    }
			});
		    }
		});
		$(element).append(unat);
	    }
	}
	else {
	    if (typeof USERNAME != 'undefined') {
		$(element).find(".attend").remove();
		var at = $("<div class='attend' event_id="+event['id']+"><span class='glyphicon glyphicon-ok' aria-hidden='true'></span><span>attend?</span></div>");
		at.click(function(e) {
		    var id = $(e.currentTarget).attr('event_id');
		    if(confirm("Are you attending?")) {
			$.ajax({
			    method: 'POST',
			    url: "http://localhost:8000/api/event/add_attendee",
			    data: {username: USERNAME,
				   event: id},
			    success: function() {
				window.location.pathname = "/calendar";
			    },
			    error: function() {
				alert("There was a problem confirming your attendance, please try again later.");
			    }
			});
		    }
		});
		$(element).append(at);
	    }	    
	}
    }

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
               "Start: "+moment(event['start']).format("LL h:mm A")+"<br>"+
               "End: "+moment(event['end']).format("LL h:mm A")+"<br>"+
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
	    data: ((typeof USERNAME) != 'undefined')?{username: USERNAME}:{},
	    success: function(data) {
		var a_events = JSON.parse(data['attending']);
		var na_events = JSON.parse(data['not_attending']);
		for (var i = 0; i < a_events.length; i++) {
		    var id = a_events[i]['pk'];
		    a_events[i] = a_events[i]['fields'];
		    a_events[i]['start'] = a_events[i]['start_datetime'];
		    a_events[i]['end'] = a_events[i]['end_datetime'];
		    a_events[i]['id'] = id;
		    a_events[i]['attending'] = true;
		    a_events[i]['title'] = a_events[i]['name'];
		}
		for (var i = 0; i < na_events.length; i++) {
		    var id = na_events[i]['pk'];
		    na_events[i] = na_events[i]['fields'];
		    na_events[i]['start'] = na_events[i]['start_datetime'];
		    na_events[i]['end'] = na_events[i]['end_datetime'];
		    na_events[i]['id'] = id;
		    na_events[i]['attending'] = false;
		    na_events[i]['title'] = na_events[i]['name'];
		}
		return a_events.concat(na_events);
	    },
            error: function() {
		alert('there was an error while fetching events!');
            },
            textColor: 'black', // a non-ajax option
	    startParam: 'start_date',
	    endParam: 'end_date'
	},
	eventAfterRender: function(event, element, view) {
	    if (view.name == "month")
		handleAttend(event, element);
	},
	eventRender: function(event, element) {
            var desc;
            printDesc(event, desc, function(event, desc, tags) {
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
	
    })

    $("#filter-button").click(function() {
	var filt = $("#filter").val();
        cur_filt = filt;
        $(".fc-event").hide(); // Hide all
        $.each($(".fc-event"), function(i, x) {
            if ($(x).attr('tag').split(' ').indexOf(filt) >= 0) {
                $(x).show(); // Show just the ones with the tags
            }
        });
    });

    var filterArea = $("#filter-area");
    filterArea.detach();
    filterArea.insertAfter(".fc-left");

});
