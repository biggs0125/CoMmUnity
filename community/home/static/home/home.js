$(document).ready(function() {
    $.ajax({
	method: 'GET',
	url: 'http://localhost:8000/api/user/events_attending',
	data: {username: USERNAME},
	success: function(data) {
	    for (var i=0; i < data.length; i++) {
		var event = data[i]['fields'];
                var tags = '';
                for(var j=0; j < events.tags.length-1; j++) {
                    tags += events.tags[j]['fields']['name'] + ", ";
                }
                tags += events.tags[j]['fields']['name'];
                var eventstuff = "<ul><li>Description: "+event.description+"</li><li>Start: "+
                    moment(event.start_datetime).format("LL h:mm")+"</li><li>End: "+
                    moment(event.end_datetime).format("LL h:mm")+"</li><li>Tags: "+
                    tags + "</li></ul>"
                var eventname = "<li><b>"+event.name+"</b>"+eventstuff+"</li>";
		$("#events_attending").append(eventname);
	    }
	}
    });
});
