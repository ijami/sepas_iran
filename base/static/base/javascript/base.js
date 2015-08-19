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
    $('.ui.checkbox').checkbox();
    var modal = $('.ui.modal');
    modal.modal();
    modal.modal('setting',{detachable:false, observeChanges: true, debug: true});
    var login_btn = $('#sign-in:not(.logged_in)');
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

jQuery(document).ready(function($){
	// browser window scroll (in pixels) after which the "back to top" link is shown
	var offset = 300,
		//browser window scroll (in pixels) after which the "back to top" link opacity is reduced
		offset_opacity = 1200,
		//duration of the top scrolling animation (in ms)
		scroll_top_duration = 700,
		//grab the "back to top" link
		$back_to_top = $('.cd-top');

	//hide or show the "back to top" link
	$(window).scroll(function(){
		( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
		if( $(this).scrollTop() > offset_opacity ) {
			$back_to_top.addClass('cd-fade-out');
		}
	});

	//smooth scroll to top
	$back_to_top.on('click', function(event){
		event.preventDefault();
		$('body,html').animate({
			scrollTop: 0 ,
		 	}, scroll_top_duration
		);
	});

});