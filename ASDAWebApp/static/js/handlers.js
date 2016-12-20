function trimInput(body) {
  var result = body.innerHTML;
  result = result.substring(0,100);
  result = result.substr(0, Math.min(result.length, result.lastIndexOf(" ")));
  result = result.replace("&lt;p&gt;","");
  result = result.replace("&lt;/p&gt;","");

  document.getElementById(body.id).innerHTML = result + " ...";
  var x = 100;
}
