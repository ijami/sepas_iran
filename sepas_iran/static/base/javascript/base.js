/**
 * Created by Javad on 7/17/2015.
 */

$(' .menu .browse .item')
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
$('.ui.search')
  .search({
    source: content
  })
;

var content = [
  { title: 'تهران' },
  { title: 'اصفهان' },
  { title: 'شیراز' },
  { title: 'تبریز' },
  { title: 'مشهد' },
  { title: 'کیش' },
  { title: 'قشم' },
  { title: 'چابهار' },
  { title: 'ارومیه' },
  { title: 'رشت' },
  { title: 'ساری' },
  { title: 'سنندج' },
];