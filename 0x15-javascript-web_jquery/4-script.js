// select DIV id #toggle_header and on click
$('#toggle_header').click(function () {
  // remove class green and add class red if green is there
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else { // remove class red and add class green
    $('header').removeClass('red').addClass('green');
  }
});
