function create_event() {
  
  $.ajax({
    url: "localhost:8000/api/event/create",
    method: "POST",
    data: {
      name: $("#event-name").text(),
      location: $("#location").text(),
      description: $("#description").text(),
      date: $("#dtpicker").text(),
      time: $("#dtpicker").text(), // uhh..gotta changed this
      tag: $("tags").value(),
      organization: #("organization").value()
    },
    error: function (){
             alert("Congrats you failed!");
           },
    success: function () {
               alert("Ermahgerd I did it!");
             }
  });

}
