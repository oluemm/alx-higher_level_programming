$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (param) {
  $('UL#list_movies').html(param.results[0].title);
});
