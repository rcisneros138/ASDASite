$("#vendorFairRegistration").submit(function(event) {
    alert("nice");
    
    $.ajax({
        url: "/forms/submitPredentalForm/",
        type: "POST",   
        data: event.serialize(),
        dataType: "json"
    });    
});