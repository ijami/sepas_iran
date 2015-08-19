/**
 * Created by Ehsan on 8/10/2015.
 */
$(document).ready(function () {
    //$('.datepicker').datepicker();
    var now = new Date();
    now.setDate(now.getDate());
    var minDate = new Date(1900, 1, 1, 0, 0, 0, 0);
    var datepicker = $('.datepicker');
    datepicker.pDatepicker({
        'format': "YYYY/MM/DD", 'observer': true, 'maxDate': now.getTime(), 'minDate': minDate.getTime(),
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


    var form = $('#register_grid form');
    $('.ui.checkbox').checkbox();
    $('.form .button').on('click', function () {
        form.form('validate form');
        form.find(".error.message ul").addClass('errorlist');
    });

    function myerror(errors) {
        var html = '<ul class="errorlist">';
        $.each(errors, function (index, value) {
            html += '<li>' + value + '</li>';
        });
        html += '</ul>';
        return $(html);
    }

    $.fn.form.settings.templates.error = myerror;

    //form.form('settings', 'templates', {'error': myerror});

    form.form({
        fields: {
            first_name: {
                identifier: 'firstname',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'لطفا نام خود را وارد کنید'
                    }
                ]
            },
            last_name: {
                identifier: 'lastname',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'لطفا نام خانوادگی خود را وارد کنید'
                    }
                ]
            },
            username: {
                identifier: 'username',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'لطفا نام کاربری را وارد کنید'
                    }
                ]
            },
            email: {
                identifier: 'email',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'لطفا ایمیل خود را وارد کنید'
                    },
                    {
                        type: 'email',
                        prompt: 'ایمیل معتبر وارد کنید'
                    }
                ]
            },
            password1: {
                identifier: 'password1',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'لطفا گذرواژه خود را وارد کنید'
                    },
                    {
                        type: 'minLength[4]',
                        prompt: 'گذرواژه باید حداقل 4 کاراکتر داشته باشد'
                    }
                ]
            },
            password2: {
                identifier: 'password2',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'لطفا تکرار گذرواژه خود را وارد کنید'
                    },
                    {
                        type: 'match[password1]',
                        prompt: 'گذرواژه ها همخوانی ندارند.'
                    }
                ]
            },
            terms: {
                identifier: 'terms',
                rules: [
                    {
                        type: 'checked',
                        prompt: 'باید با قوانین سپاس ایران موافقت کنید'
                    }
                ]
            }
        }
    });


});