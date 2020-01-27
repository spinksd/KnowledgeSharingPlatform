// This function reveals/hides the advanced search options on the home page (as well as updating the arrow type)
// This is ran the first time the page is loaded (to hide the advanced options) and in the onclick() method of the advancedOptions text
function showAdvancedOptions() {
    var elem = document.getElementById("AdvancedOptionsArea");
    var arrow = document.getElementById("AdvancedOptionsArrow");
    if (elem.style.visibility === "hidden") {
      arrow.className = "fa fa-chevron-circle-down"
      elem.style.visibility = "visible";
    } else {
      arrow.className = "fa fa-chevron-circle-left"
      elem.style.visibility = "hidden";
    }
  }