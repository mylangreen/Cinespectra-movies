let toggleBtn = document.querySelector(".menu-bar");
let dropMenu = document.querySelector(".nav-tab");
let trendingPics = document.querySelector(".trending-pics");
let slides = document.querySelectorAll(".slide");
let forwandBtn = document.querySelector(".swiper-btn");

//Dropdown function
function showMenu() {
  dropMenu.classList.toggle("drop-menu");
}

let slideIndex = 0;
let numSlides = slides.length;
function moveslide(direction) {
  slideIndex += direction;

  if (slideIndex < 0) {
    slideIndex = 0;
  } else if (slideIndex >= numSlides / (numSlides - 1)) {
    slideIndex = 0;
  }

  const offset = -slideIndex * 25;
  trendingPics.style.transform = `translateX(${offset}%)`;
}

function showTeaser(btn) {
  btn.nextElementSibling.style.display = "block";
}
function hideTeaser(btn) {
  btn.parentElement.style.display = "none";
}

function dropDown(){
  let menu = document.querySelector(".drp-menu");
  menu.classList.toggle("show");
}