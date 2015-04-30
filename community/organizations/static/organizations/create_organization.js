$(document).ready(function() {
    function orgDataCreate() {
        jQuery.ajaxSettings.traditional = true;
	var admins = $('#admins').val().split(' ');
	$.unique(admins);
	if (admins.indexOf(USERNAME) < 0) {
	    admins.push(USERNAME);
	};
	var i = admins.indexOf("");
	if (i >= 0) {
	    admins.splice(i,1);
	}
        var data = {
            name: $("#org-name").val(),
            admins: admins,
        };
        return data;
    }

    function orgPostObjectCreate() {
        var post = {
            url: "http://localhost:8000/api/organization/create",
            method: "POST",
            data: orgDataCreate(),
            success: function() {
                window.location.pathname = "/calendar";
            },
            error: function() {
                alert("One or more fields were incorrect or blank.");
            }
        };
        return post;
    }

    $("#submit").click(function() {
        $.ajax(orgPostObjectCreate());
    });
});
