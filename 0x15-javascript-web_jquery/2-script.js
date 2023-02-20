$(function () {
  // select all tags with id==red_header and add an on_click attrib
  $('#red_header').on('click', function () {
    // make the colot change to red on click
    $('header').css({ color: '#FF0000' });
  });
});
