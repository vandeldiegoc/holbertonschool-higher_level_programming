$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    data.results.forEach(function (movi){
        $('UL#list_movies').append(`<li>${movi.title}</li>`);
    })
});