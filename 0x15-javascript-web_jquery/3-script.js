$('#red_header').on('click', () => {
    if ($('header').hasClass('red')){
        console.log('Its already red mate')
    } else{
        $('header').addClass('red');
    }
});