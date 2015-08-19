/**
 * Created by Ehsan on 8/15/2015.
 */
$(document).ready(function () {
    //$('.ui.dropdown').dropdown({onChange:function(val){
    //    $('.special-form[data-tab='+val+']').show();
    //    $('.special-form[data-tab!='+val+']').hide();
    //}});
    $('.ui.dropdown').dropdown();
    $('.menu .item').tab();
    var rating = $('.field .rating');
    var degree = $('#id_degree');
    degree.attr('value', 1);
    degree.val(1);
    rating
        .rating({
            initialRating: 1,
            maxRating: 5
        });
    rating
        .rating('setting', 'onRate', function (value) {
            degree.val(value);
            degree.attr('value', value);
        });

    $('.ui.checkbox').checkbox();
});