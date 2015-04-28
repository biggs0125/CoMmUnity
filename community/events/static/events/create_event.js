$(document).ready(function() {
    $('#start_date').datepicker();
    $('#start_time').timepicker();
    $('#end_date').datepicker();
    $('#end_time').timepicker();

    function parseTime(d) {
	var ampm = d.slice(-2);
	var time = d.slice(0,-2);
	var timearray = time.split(":");
	var hour = timearray[0];
	var minute = timearray[1];
	if (ampm == "pm") {
	    if (hour != "12") {
		hour = (parseInt(hour)+12).toString();
	    }
	}
	if (ampm == "am" && hour == "12") {
	    hour = "00";
	}
	if (hour.length == 1) {
	    hour = "0" + hour;
	}
	return hour+":"+minute;
    }

    // Create data to be sent in POST request
    function eventDataCreate() {
        jQuery.ajaxSettings.traditional = true;
        var data = {
	    name: $("#event-name").val(),
      	    location: $("#location").val(),
	    description: $("#description").val(),
	    start_date: moment($("#start_date").val()).format('YYYY-MM-DD'),
	    start_time: parseTime($("#start_time").val()), 
	    end_date: moment($("#end_date").val()).format('YYYY-MM-DD'),
	    end_time: parseTime($("#end_time").val()), 
	    'tag': $('#tag').val().split(' '),
        };
        return data;
    }

    // Creates object to pass into POST request made by ajax
    function eventPostObjectCreate() {
        var post = {
	    url: "http://localhost:8000/api/event/create",
	    method: "POST",
	    data: eventDataCreate(),
	    success: function () {
		window.location.pathname = "/calendar";
	    },
	    error: function() {
		alert("One or more fields were incorrect or blank.");
	    }
	};
        return post;
    }

    $("#submit").click(function() {
	$.ajax(eventPostObjectCreate()); // Send post request
	
    });
});
	
