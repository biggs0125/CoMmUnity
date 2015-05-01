$(document).ready(function() {
    
    function handleTags(event, target) {
	$.ajax({
	    url: "http://localhost:8000/api/tag/retrieve",
	    method: "GET",
	    data: {
		id: event['tags']
	    },
	    success: function (tagNames) {
		var tags = '';
		// Append the tag names to description
		for (var i = 0; i < tagNames.length-1; i++) {
		    tags += tagNames[i]['fields']['name'] + ", ";
		}
		tags += tagNames[tagNames.length-1]['fields']['name'];
		var eventstuff = "<div class='attending'><ul class='attending-description'><li>Description: "+event.description+"</li><li>Start: "+
		    moment(event.start_datetime).format("LL h:mm A")+"</li><li>End: "+
		    moment(event.end_datetime).format("LL h:mm A")+"</li><li>Tags: "+
		    tags + "</li></ul></div>"
		var eventname = "<li><b class='event-title'>"+event['name']+"</b>"+eventstuff+"</li>";
		target.append(eventname);
		
	    },
	});
    }

    jQuery.ajaxSettings.traditional = true;
    $.ajax({
	method: 'GET',
	url: 'http://localhost:8000/api/user/events_attending',
	data: {username: USERNAME},
	success: function(data) {
	    for (var i=0; i < data.length; i++) {
		var event = data[i]['fields'];
		handleTags(event, $("#events-attending"));
	    }
	}
    });
    
    $.ajax({
	method: 'GET',
	url: 'http://localhost:8000/api/event/subscribed_events',
	data: {username: USERNAME},
	success: function(data) {
	    for (var i=0; i < data.length; i++) {
		var event = data[i]['fields'];
		handleTags(event, $("#subscribed-events"));
	    }
	}
    });
    
});
