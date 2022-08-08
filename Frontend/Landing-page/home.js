//This part is for the responsiveness of the navigation on mobile view and allows the hambuger to function well.
//This is for the hamburger menu
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
});

document.querySelectorAll(".nav-link").forEach((n) =>
  n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
  })
);

//js code for the accordion
const accordionItemHeaders = document.querySelectorAll(
  ".accordion-item-header"
);

accordionItemHeaders.forEach((accordionItemHeaders) => {
  accordionItemHeaders.addEventListener("click", (event) => {
    accordionItemHeaders.classList.toggle("active");
    const accordionItemBody = accordionItemHeaders.nextElementSibling;
    if (accordionItemHeaders.classList.contains("active")) {
      accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
    } else {
      accordionItemBody.style.maxHeight = 0;
    }
  });
});
/*This is for the scroll back to top button
const scrollBtn = document.querySelector(".scroll-to-top")

scrollBtn.addEventListener("click", () => {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});

document.addEventListener("scroll", (e) => {
  if (document.documentElement.scrollTop <= 5000) {
    scrollBtn.style.display = "none";
  } else {
    scrollBtn.style.display = "block";
  }
});*/
