$(document).ready(function() {
    $('#start_date').datepicker();
    $('#start_time').timepicker();
    $('#end_date').datepicker();
    $('#end_time').timepicker();

    $("#submit").click(function() {

	$.ajax({
	    url: "http://localhost:8000/api/event/create",
	    method: "POST",
	    data: {
		name: $("#event-name").val(),
		location: $("#location").val(),
		description: $("#description").val(),
		start_date: moment($("#start_date").val()).format('YYYY-MM-DD'),
		start_time: moment($("#start_time").val()).format('HH:mm'), 
		end_date: moment($("#end_date").val()).format('YYYY-MM-DD'),
		end_time: moment($("#end_time").val()).format('HH:mm'), 
		//tag: $("#tags").val(),
		//organization: $("#organization").val()
	    },
	    success: function () {
		window.location.pathname = "/calendar";
	    },
	    error: function() {
		alert("One or more fields were incorrect or blank.");
	    }
	});
	
    });
});
	
