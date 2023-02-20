// get the json contents of the endpoint, pass it as args `data` into the func
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  // Display the name in DIV with id #character
  $('DIV#character').html(data.name);
});
