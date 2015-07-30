/**
 * Created by Javad on 7/17/2015.
 */



$('.ui.search')
    .search({
        source: content
    })
;

var content = [
    {title: 'تهران'},
    {title: 'اصفهان'},
    {title: 'شیراز'},
    {title: 'تبریز'},
    {title: 'مشهد'},
    {title: 'کیش'},
    {title: 'قشم'},
    {title: 'چابهار'},
    {title: 'ارومیه'},
    {title: 'رشت'},
    {title: 'ساری'},
    {title: 'سنندج'},
];

$(document).ready(function () {
    var modal = $('.ui.modal');
    modal.modal();
    modal.modal('setting',{detachable:false, observeChanges: true, debug: true});
    var login_btn = $('#sign-in');
    login_btn.on('click', function () {
        modal.modal('show');
        console.log("saka");
    });

    $('.browse')
  .popup({
    inline   : true,
    hoverable: true,
    position : 'bottom left',
    delay: {
      show: 300,
      hide: 800
    }
  })
;
});
