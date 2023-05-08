/* with jQuery
$(document).ready(function () {
    $('header').css('color', 'red');
    console.log($('header').text())
});
*/

// without jQuery
document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('header').style.color = 'red';
});
