// closing of alert


const submitBtn = document.getElementsByTagName("input[type=submit]");

submitBtn.addEventListener("click", function () {
  console.log("click");
  document.getElementsByClassName("spinner__background").style.display =
    "block";
});
console.log('working testingsd')

setTimeout(function () {
  document.getElementsByClassName("spinner__background").style.display = "none";
}, 6000);



setTimeout(function () {
  document.getElementById("alert").style.display = "none";
}, 6000);

