#!/usr/bin/node
// script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello f
// from that fetch in the HTML tag DIV#hello.

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
