/**
 * Created by po0ya on 9/08/15.
 */

$(document).ready(function(){

    var $serach_box = $('.auto-complete').children();
    var csrf = $("input[name=csrfmiddlewaretoken]").val();

    $serach_box.on('input', function(){
        var $results = $('#results');
        $results.html('');
        search(this.value, this);
    });

    function search(str, man) {
        $.ajax({
            url: 'search/',
            method: 'POST',
            data: {
                'name': str,
                'csrfmiddlewaretoken': csrf
            },
            success: function(response) {
                var results = response.result;
                var $results = $('#results');
                $.each(results, function( index, value ) {
                    $('<li/>').html(value).appendTo($results).click(function () {
                        $results.html('');
                        $(man).val(value);
                    });
                });

//                alert(response.charCode);
            }
        });
    }
});

