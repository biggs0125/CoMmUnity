$(document).ready(function() {
  $("#submit").click(function() {
    alert("Hello!"); 
    console.log('name:' + $("#event-name").val());
    $.ajax({
      url: "http://localhost:8000/api/event/create",
      method: "POST",
      data: {
        name: $("#event-name").val(),
      location: $("#location").val(),
      description: $("#description").val(),
      date: $("#dtpicker").val().split(' ')[0],
      time: $("#dtpicker").val().split(' ')[1], 
      tag: $("#tags").val(),
      //organization: $("#organization").val()
      },
      error: function (){
               alert("Congrats you failed!");
             },
      success: function () {
                 alert("Ermahgerd I did it!");
               }
    });

  });
});
