new Swiper('.programs-slider', {
  // Optional parameters
  direction: 'horizontal',
  spaceBetween: 30,

  slidesPerView: 3,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  breakpoints: {
    1200: {
      slidesPerView: 3,
    },
    768: {
      slidesPerView: 2,
    },
    300: {
      slidesPerView: 1,
    },
  }

});

new Swiper(".feedback-slider", {
  effect: "cards",
  grabCursor: true,
});