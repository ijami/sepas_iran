$(document).ready(function () {
    //$('.datepicker').datepicker();
    var maxDate = new Date(2115, 1, 1);
    var minDate = new Date(2015, 1, 1, 0, 0, 0, 0);
    var datepicker = $('.datepicker');
    datepicker.pDatepicker({
        'format': "YYYY/MM/DD", 'observer': true, 'maxDate': maxDate.getTime(), 'minDate': minDate,
        'justSelectOnDate': true
    });



    var dateValue = datepicker.attr('value');
    if (dateValue) {
        var year;
        var month;
        var day;
        if (datepicker.parent().hasClass("error")) {
            try {
                datepicker.pDatepicker("goToday");
            } catch (err) {
                console.log(err);
            }
        } else {
            console.log("s2");
            var splitted = dateValue.split("/");
            year = parseInt(splitted[0]);
            month = parseInt(splitted[1]);
            day = parseInt(splitted[2]);
            try {
                datepicker.pDatepicker("setDate", [year, month, day, 0, 0])
            } catch (err) {
                console.log(err);
            }
        }
    }


});