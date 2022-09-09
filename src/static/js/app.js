//Country Codes 
import intlTelInput from "intl-tel-input";
if (document.querySelector("#mobile_code")) {
  const input = document.querySelector("#mobile_code");
  intlTelInput(input, {
    initialCountry: "gh",
    utilsScript:
      "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.4/js/utils.js",
  });
}
//
setTimeout(function(){
  $('#message').fadeOut('slow')
}, 4000)

//Move cursor to the next in the OTP input
if (document.getElementsByClassName("otp-input")[0]){
  var container = document.getElementsByClassName("otp-input")[0];
container.onkeyup = function(e) {
    var target = e.srcElement || e.target;
    var maxLength = parseInt(target.attributes["maxlength"].value, 10);
    var myLength = target.value.length;
    if (myLength >= maxLength) {
        var next = target;
        while (next = next.nextElementSibling) {
            if (next == null)
                break;
            if (next.tagName.toLowerCase() === "input") {
                next.focus();
                break;
            }
        }
    }
    // Move to previous field if empty (user pressed backspace)
    else if (myLength === 0) {
        var previous = target;
        while (previous = previous.previousElementSibling) {
            if (previous == null)
                break;
            if (previous.tagName.toLowerCase() === "input") {
                previous.focus();
                break;
            }
        }
    }
}
}
