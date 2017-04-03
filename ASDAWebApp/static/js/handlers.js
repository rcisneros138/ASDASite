function trimInput(body) {
  var result = body.innerHTML;
  result = result.substring(0,100);
  result = result.substr(0, Math.min(result.length, result.lastIndexOf(" ")));
  result = result.replace("&lt;p&gt;","");
  result = result.replace("&lt;/p&gt;","");

  document.getElementById(body.id).innerHTML = result + " ...";
  var x = 100;
}

$("#submitSignUp").click(function(e){
    page = $(event.target).attr('id');
    console.log(page)
    $('#signUpForm').submit(function(e){
        e.preventDefault();
        $.post('/submitPredentalForm/', $(this).serialize(), function(data){
          var html = ""
          html += data
          $("#return").html(html);
        });
    });
});

$(".formNext").click(function() {
  page = $(event.target).attr('id');
  if(page == "submitpage1"){
    $("#PreDentalpage1").addClass("hidden");
    $("#PreDentalpage2").removeClass("hidden");
  }
  else if (page == "submitpage2") {
    $("#PreDentalpage2").addClass("hidden");
    $("#PreDentalpage3").removeClass("hidden");
  }

});

$(".formBack").click(function() {
  page = $(event.target).attr('id');
  if(page == "backpage2"){
    $("#PreDentalpage1").removeClass("hidden");
    $("#PreDentalpage2").addClass("hidden");
  }
  else if (page == "backpage3") {
    $("#PreDentalpage2").removeClass("hidden");
    $("#PreDentalpage3").addClass("hidden");
  }
});
