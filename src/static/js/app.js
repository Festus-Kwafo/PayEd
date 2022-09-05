import intlTelInput from "intl-tel-input";
if (document.querySelector("#mobile_code")) {
  const input = document.querySelector("#mobile_code");
  intlTelInput(input, {
    initialCountry: "gh",
    utilsScript:
      "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.4/js/utils.js",
  });
}
