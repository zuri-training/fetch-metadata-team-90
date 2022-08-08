const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav__mobile-list");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("avtive");
  navMenu.classList.toggle("avtive");
});
