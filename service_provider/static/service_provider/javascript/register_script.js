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
                identifier: 'first_name',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'لطفا نام خود را وارد کنید'
                    }
                ]
            },
            last_name: {
                identifier: 'last_name',
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
                        prompt: 'گذرواژه باید حداقل 8 کاراکتر داشته باشد'
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