$(document).ready(function() {
  $("#submit").click(function() {
    console.log('name:' + $("#event-name").val());
    console.log('date:' + $("#dtpicker input").val().split(' ')[0]);
    console.log('time:' + $("#dtpicker input").val().split(' ')[1]);

    var dt = moment($("#dtpicker input").val()).format('YYYY-MM-DD HH:mm');

    $.ajax({
      url: "http://localhost:8000/api/event/create",
      method: "POST",
      data: {
        name: $("#event-name").val(),
      location: $("#location").val(),
      description: $("#description").val(),
      //date: moment($("#dtpicker input").val().split(' ')[0]).format('YYYY-MM-DD'),
      //time: moment($("#dtpicker input").val().split(' ')[1]).format('HH:mm'), 
      date: dt.split(' ')[0],
      time: dt.split(' ')[1], 
      //tag: $("#tags").val(),
      //organization: $("#organization").val()
      },
      error: function (){
               console.log("Congrats you failed!");
             },
      success: function () {
                 console.log("Ermahgerd I did it!");
               }
    });

  });
});
