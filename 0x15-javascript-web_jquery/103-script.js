$(document).ready(function () {
  const langCode = $('input#language_code').val();
  const API_URL = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;
  $('input#btn_translate').on('click kepress', (event) => {
    // console.log($('input#language_code').val());
    // console.log(langCode);
    // console.log(API_URL);
    if (event.type === 'click' || (event.type === 'keypress' && event.keyCode === 13)) {
      $.get(API_URL, (reponse, statusCode) => {
        $('div#hello').text(reponse.hello);
      });
    }
  });
});
