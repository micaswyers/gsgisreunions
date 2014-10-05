$(document).ready(function() {
    console.log('ready!');
    $(".hidden").hide();
    });

$(window).scroll(function() {
if ($(this).scrollTop() > 1){
        $('header').addClass("sticky");
    $(".hidden").show();
          }
  else{
          $('header').removeClass("sticky");
        $(".hidden").hide();
            }
});
