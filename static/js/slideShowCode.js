

/* starting with the first slide/image */
var slideNo = 0;
slideShow(slideNo);

/*following function passes the slideNo to display current slide*/
function currSlide (n) {
  slideShow(slideN0 = n);
}
/* TO-DO: function to increment slideNo:
          Link it to Next button/class */
function nextSlide(n){
     // increment n and pass it to slideShow
     slideNo = slideNo + n;
     slideShow(slideNo); 
}
  /* To-Do: function to decrement slideNo
          Link it to Prev button/class */
function prevSlide(n) {
  // 
  slideNo = slideNo -n ;
  slideShow(slideNo);
}

/*following function is for the slide show */
function slideShow (n){
/*  1- Assign all the images to a variable */
    var x = document.getElementsByClassName("images");
/*
    Things to consider, 
    because of next button:What if your current slide Number exceeds the total slides? 
        What should happen at that point?
    because of prev button: what if current slide number goes 
    below your first slide number
   */

   if(n < 0) {
      slideNo = x.length -1 ; 
     }
   if (n > x.length-1) /*when n is > then 4 */{
      slideNo = 0;
   }
/*    2- In a for loop, hide all the images using the above variable by 
      changing the display property */

    for (var i=0; i < x.length; i++){
    //starting at 0 up to 3. hide all images
      x[i].style.display="none";
  }
/*    3- Change the display property of one image at a time */
//.first time, n[0] is displayed as block
    
    x[slideNo].style.display = "block";
}
/**************************END OF SLIDE SHOW ASSIGNMENT***********************************************/

/****************************************************************************************************/
