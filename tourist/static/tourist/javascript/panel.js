/**
 * Created by Javad on 7/30/2015.
 */

$(document).ready(function(){
    $('.special.cards .image').dimmer({
        on: 'hover'
    });
});

$('#button').click(function(){
   $("input[type='file']").trigger('click');
})

$("input[type='file']").change(function(){
   $('#val').text(this.value.replace(/C:\\fakepath\\/i, ''))
})