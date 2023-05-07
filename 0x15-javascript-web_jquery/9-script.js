$(document).ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (response, statusCode) => {
        // console.log(response)
        $('#hello').text(response['hello']);
    });
});