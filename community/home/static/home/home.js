$(document).ready(function() {
    $.ajax({
	method: 'GET',
	url: 'http://localhost:8000/api/user/events_attending',
	data: {username: USERNAME},
	success: function(data) {
	    for (var i=0; i < data.length; i++) {
		var event = data[i]['fields'];
		$("#events_attending").append("<li>"+event.name+"</li>");
	    }
	}
    });
});
