// $('h1').click(function(){
//   console.log('There was a click!');
//   $(this).text("I was changed!")
// })
//
//
// $('li').click(function(){
//   console.log("an li item was clicked!");
// })
//

//key press
// $('input').eq(0).keypress(function(event){
//   $('h3').toggleClass('turnBlue');
//   console.log(event);
// })


$('input').eq(0).keypress(function(event){
  if (event.which === 13) {
    $('h3').toggleClass('turnBlue');
  }
})


// on() method
$('h1').on('dblclick',function(){
  $(this).toggleClass('turnBlue');
})

$('li').on('mouseenter',function(){
  $(this).toggleClass('turnRed');
})


// $('input').eq(1).on('click',function(){
//   $('.container').fadeOut(3000)
// })

$('input').eq(1).on('click',function(){
  $('.container').slideUp(3000)
})
