$('.owl-carousel').owlCarousel({
  autoplay:true,
  autoplayhover:true,
  autoplaytimeout:100,
  margin:50,


  responsive:{
      0:{
          items:1,
          nav:true
      },
      500:{
          items:2,
          nav:true
      },
      1000:{
          items:3,
          nav:true,
         dots:true,
      }
  }
})

