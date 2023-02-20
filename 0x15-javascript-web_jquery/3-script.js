$(function () {
  // select all tags with id==red_header and add an on_click attrib
  $('#red_header').on('click', function () {
    // adds the class red to the <header>
    $('header').addClass('red');
  });
});
