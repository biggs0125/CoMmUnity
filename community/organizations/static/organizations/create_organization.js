$(document).ready(function() {
    function orgDataCreate() {
        jQuery.ajaxSettings.traditional = true;
        var data = {
            name: $("#org-name").val(),
            'admins': $('#admins').val().split(' '),
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
            }
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
