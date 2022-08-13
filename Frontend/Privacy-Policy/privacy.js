/*This is for the scroll back to top button*/
const scrollBtn = document.querySelector(".scroll-to-top");

const refreshButtonVisibility = () => {
  var scrolltotal = document.documentElement.scroll;
  if (document.documentElement.scrollTop <= 1000) {
    scrollBtn.style.display = "none";
  } else {
    scrollBtn.style.display = "block";
  }
};
refreshButtonVisibility();

scrollBtn.addEventListener("click", () => {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});

document.addEventListener("scroll", (e) => {
  refreshButtonVisibility();
});
