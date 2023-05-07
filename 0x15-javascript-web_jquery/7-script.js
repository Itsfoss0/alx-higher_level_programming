$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (response, code) => {
  // console.log(response);
  $('#character').text(response.name);
});
