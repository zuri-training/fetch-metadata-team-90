/*This is for the scroll back to top button*/
/*Just copy and paste in your .js file. If you don't have .js file, create one and link 
at the bottom of your html, before footer, using link for js stylesheet (<script src=""></script>)*/
const scrollBtn = document.querySelector(".scroll-to-top")

const refreshButtonVisibility = () => {
  var scrolltotal = document.documentElement.scroll
  if (document.documentElement.scrollTop <= 3000) {
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
