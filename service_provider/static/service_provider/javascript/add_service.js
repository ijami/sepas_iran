/**
 * Created by Ehsan on 8/10/2015.
 */
$(document).ready(function () {
    //$('.datepicker').datepicker();
    var now = new Date();
    now.setDate(now.getDate());
    var datepicker = $('.datepicker');
    datepicker.pDatepicker({
        'format': "YYYY/MM/DD", 'observer': true, 'minDate': now.getTime(),
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

});/**
 * Created by MJR on 8/16/2015.
 */
