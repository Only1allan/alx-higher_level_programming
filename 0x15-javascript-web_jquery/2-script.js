#!/usr/bin/node
// script updating text color of header to red
// when users click on the tag DIV#red_header

$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
