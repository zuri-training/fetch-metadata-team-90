 /*This is the javascript code for the preloader*/
 /*If "main" does not work, replace with "body". Then input these in the 
 class in your css: opacity: 0; | display: none; | transition: opacity 1s ease-in; */
 const loader = document.querySelector('.loader');
 const main = document.querySelector('.main');

 function init() {
     setTimeout(() => {
         loader.style.opacity = 0;
         loader.style.display = 'none';

         main.style.display = 'block';
         setTimeout(() => main.style.opacity = 1, 50);
     }, 4000);
}

init();


 