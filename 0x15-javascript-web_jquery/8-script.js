// get json data
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $(data.results).each(function (i) { // loop thru the results dict
    $('#list_movies').prepend('<li>' + this.title + '</li>'); // add the title of each dict to the list
  });
});
