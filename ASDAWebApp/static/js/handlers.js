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
  requiredList = ["Name", "Phone", "Address1", "Email", "BirthDate", "School", "Year",
  "EmergName", "EmergPhone", "EmergEmail",
  "SocialEvent", "DietaryNeeds",
  "cardHolderName", "cardNumber", "cvv"];

  failedInputs = []
  for(item in requiredList){
    element = requiredList[item];
    elementSelector = $("input[name=" + element + "]");
    $(elementSelector).parent().removeClass("has-error");
    if(elementSelector.val() == ""){
      failedInputs.push(element);
      // focusPage(elementSelector, 1);
      $(elementSelector).parent().addClass("has-error");
    }
  }
  if(failedInputs.length == 0){
    console.log("POST sent");
    $("#inputFailure").addClass("hidden");
    $.ajax({
        url : "/submitPredentalForm/",
        type: "POST",
        data : $('#preDentalSignUpForm').serialize() + "&csrfmiddlewaretoken=" + document.getElementsByName('csrfmiddlewaretoken')[0].value,
        dataType : "json",
        success: function( data ){
          if(data["response"] == "Successful"){
              // location.reload();
                console.log("Successful");
          }
          else{
            console.log(data);
          }
        }
    });
  }
  else{
    $("#inputFailure").removeClass("hidden");
    console.log("Inputs not ready for POST...");
    console.log(failedInputs);
  }
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

function pageChange(targetPage) {
  if(targetPage == "1" ||targetPage == 1){
    $("#PreDentalpage1").removeClass("hidden");
    $("#PreDentalpage2").addClass("hidden");
    $("#PreDentalpage3").addClass("hidden");
  }
  else if(targetPage == "2" ||targetPage == 2){
    $("#PreDentalpage1").addClass("hidden");
    $("#PreDentalpage2").removeClass("hidden");
    $("#PreDentalpage3").addClass("hidden");
  }
  else if(targetPage == "3" ||targetPage == 3){
    $("#PreDentalpage1").addClass("hidden");
    $("#PreDentalpage2").addClass("hidden");
    $("#PreDentalpage3").removeClass("hidden");
  }

}

function focusPage(input, pageNumber) {
  pageChange(pageNumber);

}
