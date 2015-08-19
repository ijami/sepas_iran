/**
 * Created by po0ya on 9/08/15.
 */

$(document).ready(function(){

    var $serach_box = $('.auto-complete').children();
    var csrf = $("input[name=csrfmiddlewaretoken]").val();

    $serach_box.on('input', function(){
        search(this.value);
    });

    function search(str) {
        $.ajax({
            url: 'search/',
            method: 'POST',
            data: {
                'name': str,
                'csrfmiddlewaretoken': csrf
            },
            success: function(response) {
                alert(response);
            }
        });
    }
});

