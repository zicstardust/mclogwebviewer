function hideshowDiv(id="logs_list") {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
    document.getElementById("hideshowbutton").innerHTML = "Hide Logs";
  } else {
    x.style.display = "none";
    document.getElementById("hideshowbutton").innerHTML = "Show Logs";
  }
} 


function scrollheight(id){
  var elem = document.getElementById(id);
  elem.scrollTop = elem.scrollHeight;
}