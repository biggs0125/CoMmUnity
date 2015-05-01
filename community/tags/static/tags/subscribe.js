$(document).ready(function() {

    $('#selecter').chosen({width: "250px", opacity: "1.0"});
    
    $.ajax({
	method: "GET",
	url: "http://localhost:8000/api/tag/retrieve",
	data: {username: USERNAME},
	success: function(tags) {
	    for(var i=0; i<tags.length; i++) {
		var tag = tags[i]['fields'];
		if (!tag['is_org_tag']) {
		    $("#tags").append("<option value='"+tag['name']+"'>"+tag['name']+"</option>");
		}
	    }
	    $("#selecter").trigger('chosen:updated');
	}
    });

    $.ajax({
	method: "GET",
	url: "http://localhost:8000/api/organization/retrieve",
	success: function(orgs) {
	    for(var i=0; i<orgs.length; i++) {
		var org = orgs[i]['fields'];
		$("#orgs").append("<option value='"+org['name']+"'>"+org['name']+"</option>");
	    }
	    $("#selecter").trigger('chosen:updated');
	}
    });

    $("#submit").click(function() {
	jQuery.ajaxSettings.traditional = true;
	$.ajax({
	    method: "POST",
	    url: "http://localhost:8000/api/user/add_subscriptions",
	    data:{
		username: USERNAME,
		tag: $("#selecter").val(),
	    },
	    success: function() {
		window.location.pathname = "/home";
	    },
	    error: function() {
		alert("There was an error saving your subscriptions, try again later.");
	    }
	});
    });

});
