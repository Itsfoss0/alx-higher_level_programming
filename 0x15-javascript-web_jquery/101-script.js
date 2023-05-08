$(document).ready(function () {
  $('#add_item').on('click', () => {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').on('click', () => {
    $('.my_list').find('li').last().remove();
  });

  $('#clear_list').on('click', () => {
    $('.my_list').remove();
  });
});
