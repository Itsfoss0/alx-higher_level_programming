$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response, statusCode){
    const rdata = response['results'];
    for (let i = 0; 0 < rdata.length; i++){
        $('#list_movies').append(`<li>${rdata[i]['title']}</li>`)
        console.log(rdata[i]['title']);
    }
});