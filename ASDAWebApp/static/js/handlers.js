function trimInput(body) {
  var result = body.innerHTML;
  result = result.substring(0,150);
  result = result.replace("&lt;p&gt;","");
  result = result.replace("&lt;/p&gt;","");
  document.getElementById(body.id).innerHTML = result;
  var x = 100;
}
