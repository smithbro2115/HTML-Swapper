import unittest
from Converter.converter import Converter
import bs4
from Converter import Rules


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()
        self.html = """
<!DOCTYPE html>
<html lang="en-US">
<head>
	<meta charset="UTF-8" />
<meta name="keywords" content="audio theatre, audio theater, audio drama, christian radio drama, christian audio drama, missionary audio theater, missionary audio drama, christian radio theater," /><meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link rel="pingback" href="https://brinkmanadventures.com/xmlrpc.php" />

	<script type="text/javascript">
		document.documentElement.className = 'js';
	</script>

	<script>var et_site_url='https://brinkmanadventures.com';var et_post_id='5215';function et_core_page_resource_fallback(a,b){"undefined"===typeof b&&(b=a.sheet.cssRules&&0===a.sheet.cssRules.length);b&&(a.onerror=null,a.onload=null,a.href?a.href=et_site_url+"/?et_core_page_resource="+a.id+et_post_id:a.src&&(a.src=et_site_url+"/?et_core_page_resource="+a.id+et_post_id))}
</script><title>Brinkman Adventures | Family Audio Drama</title>
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel='dns-prefetch' href='//s.w.org' />
<link rel="alternate" type="application/rss+xml" title="Brinkman Adventures &raquo; Feed" href="https://brinkmanadventures.com/feed" />
<link rel="alternate" type="application/rss+xml" title="Brinkman Adventures &raquo; Comments Feed" href="https://brinkmanadventures.com/comments/feed" />
		<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/11.2.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/11.2.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/brinkmanadventures.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.1"}};
			!function(a,b,c){function d(a,b){var c=String.fromCharCode;l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,a),0,0);var d=k.toDataURL();l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,b),0,0);var e=k.toDataURL();return d===e}function e(a){var b;if(!l||!l.fillText)return!1;switch(l.textBaseline="top",l.font="600 32px Arial",a){case"flag":return!(b=d([55356,56826,55356,56819],[55356,56826,8203,55356,56819]))&&(b=d([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]),!b);case"emoji":return b=d([55358,56760,9792,65039],[55358,56760,8203,9792,65039]),!b}return!1}function f(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var g,h,i,j,k=b.createElement("canvas"),l=k.getContext&&k.getContext("2d");for(j=Array("flag","emoji"),c.supports={everything:!0,everythingExceptFlag:!0},i=0;i<j.length;i++)c.supports[j[i]]=e(j[i]),c.supports.everything=c.supports.everything&&c.supports[j[i]],"flag"!==j[i]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[j[i]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(h=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",h,!1),a.addEventListener("load",h,!1)):(a.attachEvent("onload",h),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),g=c.source||{},g.concatemoji?f(g.concatemoji):g.wpemoji&&g.twemoji&&(f(g.twemoji),f(g.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
		<meta content="Divi Child v.1.0.0" name="generator"/><style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
	<link rel='stylesheet' id='wp-block-library-css'  href='https://brinkmanadventures.com/wp-includes/css/dist/block-library/style.min.css?ver=5.1' type='text/css' media='all' />
<link rel='stylesheet' id='lity-css-css'  href='https://brinkmanadventures.com/wp-content/plugins/flowpaper-lite-pdf-flipbook/assets/lity/lity.min.css' type='text/css' media='all' />
<link rel='stylesheet' id='vfb-pro-css'  href='https://brinkmanadventures.com/wp-content/plugins/vfb-pro/public/assets/css/vfb-style.min.css?ver=2018.08.01' type='text/css' media='all' />
<link rel='stylesheet' id='wpmenucart-icons-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce-menu-bar-cart/css/wpmenucart-icons.css?ver=5.1' type='text/css' media='all' />
<link rel='stylesheet' id='wpmenucart-fontawesome-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce-menu-bar-cart/css/wpmenucart-fontawesome.css?ver=5.1' type='text/css' media='all' />
<link rel='stylesheet' id='wpmenucart-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce-menu-bar-cart/css/wpmenucart-main.css?ver=5.1' type='text/css' media='all' />
<link rel='stylesheet' id='woocommerce-layout-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/css/woocommerce-layout.css?ver=3.5.5' type='text/css' media='all' />
<link rel='stylesheet' id='woocommerce-smallscreen-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/css/woocommerce-smallscreen.css?ver=3.5.5' type='text/css' media='only screen and (max-width: 768px)' />
<link rel='stylesheet' id='woocommerce-general-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/css/woocommerce.css?ver=3.5.5' type='text/css' media='all' />
<style id='woocommerce-inline-inline-css' type='text/css'>
.woocommerce form .form-row .required { visibility: visible; }
</style>
<link rel='stylesheet' id='albdesign-wc-donation-frontend-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce_donations_on_cart/assets/css/frontend.css?ver=5.1' type='text/css' media='all' />
<link rel='stylesheet' id='xoo-cp-style-css'  href='https://brinkmanadventures.com/wp-content/plugins/added-to-cart-popup-woocommerce/assets/css/xoo-cp-style.css?ver=1.4' type='text/css' media='all' />
<style id='xoo-cp-style-inline-css' type='text/css'>
td.xoo-cp-pqty{
			    min-width: 120px;
			}.xoo-cp-adding,.xoo-cp-added{display:none!important}
			.xoo-cp-container{
				max-width: 650px;
			}
			.xcp-btn{
				background-color: #777777;
				color: #ffffff;
				font-size: 14px;
				border-radius: 5px;
				border: 1px solid #777777;
			}
			.xcp-btn:hover{
				color: #ffffff;
			}
			td.xoo-cp-pimg{
				width: 20%;
			}
			table.xoo-cp-pdetails , table.xoo-cp-pdetails tr{
				border: 0!important;
			}
			table.xoo-cp-pdetails td{
				border-style: solid;
				border-width: 0px;
				border-color: #ebe9eb;
			}
</style>
<link rel='stylesheet' id='woocommerce-nyp-css'  href='https://brinkmanadventures.com/wp-content/plugins/woocommerce-name-your-price/assets/css/name-your-price.css?ver=2.4.2' type='text/css' media='all' />
<link rel='stylesheet' id='parent-style-css'  href='https://brinkmanadventures.com/wp-content/themes/Divi/style.css?ver=5.1' type='text/css' media='all' />
<link rel='stylesheet' id='child-style-css'  href='https://brinkmanadventures.com/wp-content/themes/Divi-Child/style.css?ver=1.0.0' type='text/css' media='all' />
<link rel='stylesheet' id='divi-fonts-css'  href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800&#038;subset=latin,latin-ext' type='text/css' media='all' />
<link rel='stylesheet' id='divi-style-css'  href='https://brinkmanadventures.com/wp-content/themes/Divi-Child/style.css?ver=3.19.15' type='text/css' media='all' />
<link rel='stylesheet' id='wp-members-css'  href='https://brinkmanadventures.com/wp-content/plugins/wp-members/css/generic-no-float.css?ver=3.2.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='et-builder-googlefonts-cached-css'  href='https://fonts.googleapis.com/css?family=Source+Sans+Pro%3A200%2C200italic%2C300%2C300italic%2Cregular%2Citalic%2C600%2C600italic%2C700%2C700italic%2C900%2C900italic&#038;ver=5.1#038;subset=cyrillic,greek,vietnamese,latin,greek-ext,latin-ext,cyrillic-ext' type='text/css' media='all' />
<link rel='stylesheet' id='tawcvs-frontend-css'  href='https://brinkmanadventures.com/wp-content/plugins/variation-swatches-for-woocommerce/assets/css/frontend.css?ver=20160615' type='text/css' media='all' />
<link rel='stylesheet' id='mc4wp-form-basic-css'  href='https://brinkmanadventures.com/wp-content/plugins/mailchimp-for-wp/assets/css/form-basic.min.css?ver=4.3.3' type='text/css' media='all' />
<link rel='stylesheet' id='dashicons-css'  href='https://brinkmanadventures.com/wp-includes/css/dashicons.min.css?ver=5.1' type='text/css' media='all' />
<link rel='stylesheet' id='sb_divi_fe_custom_css-css'  href='https://brinkmanadventures.com/wp-content/plugins/divi_layout_injector/style.css?ver=5.1' type='text/css' media='all' />
<script type='text/javascript' src='https://brinkmanadventures.com/wp-includes/js/jquery/jquery.js?ver=1.12.4'></script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1'></script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/flowpaper-lite-pdf-flipbook/assets/lity/lity.min.js'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var wpmenucart_ajax_assist = {"shop_plugin":"woocommerce","always_display":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/woocommerce-menu-bar-cart/javascript/wpmenucart-ajax-assist.js?ver=5.1'></script>
<link rel='https://api.w.org/' href='https://brinkmanadventures.com/wp-json/' />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://brinkmanadventures.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://brinkmanadventures.com/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress 5.1" />
<meta name="generator" content="WooCommerce 3.5.5" />
<link rel="canonical" href="https://brinkmanadventures.com/" />
<link rel='shortlink' href='https://brinkmanadventures.com/' />
<link rel="alternate" type="application/json+oembed" href="https://brinkmanadventures.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fbrinkmanadventures.com%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://brinkmanadventures.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fbrinkmanadventures.com%2F&#038;format=xml" />
<meta name="p:domain_verify" content="a1e8fe2bf71f3aabddfa7b6d770a121c"/>
<script type="text/javascript"><!--
function powerpress_pinw(pinw_url){window.open(pinw_url, 'PowerPressPlayer','toolbar=0,status=0,resizable=1,width=460,height=320');	return false;}
//-->
</script>
<style type="text/css">#wpadminbar #wp-admin-bar-vfbp-toolbar-edit-form > .ab-item:before {content: "\f175";top: 2px;}#wpadminbar #wp-admin-bar-vfbp-admin-toolbar > .ab-item:before {content: "\f175";top: 2px;}</style><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" /><link rel="shortcut icon" href="https://brinkmanadventures.com/wp-content/uploads/2016/10/faviconv4.png" />	<noscript><style>.woocommerce-product-gallery{ opacity: 1 !important; }</style></noscript>
	<!-- Global Site Tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-72806957-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-72806957-1');
</script>
<link rel="stylesheet" id="et-divi-customizer-global-cached-inline-styles" href="https://brinkmanadventures.com/wp-content/cache/et/global/et-divi-customizer-global-15507893621659.min.css" onerror="et_core_page_resource_fallback(this, true)" onload="et_core_page_resource_fallback(this)" /><!-- WooCommerce Colors -->
<style type="text/css">
p.demo_store{background-color:#2ea3f2;color:#fff;}.woocommerce small.note{color:#777;}.woocommerce .woocommerce-breadcrumb{color:#777;}.woocommerce .woocommerce-breadcrumb a{color:#777;}.woocommerce div.product span.price,.woocommerce div.product p.price{color:#2ea3f2;}.woocommerce div.product .stock{color:#2ea3f2;}.woocommerce span.onsale{background-color:#2ea3f2;color:#fff;}.woocommerce ul.products li.product .price{color:#2ea3f2;}.woocommerce ul.products li.product .price .from{color:rgba(129, 147, 159, 0.5);}.woocommerce nav.woocommerce-pagination ul{border:1px solid #d3ced3;}.woocommerce nav.woocommerce-pagination ul li{border-right:1px solid #d3ced3;}.woocommerce nav.woocommerce-pagination ul li span.current,.woocommerce nav.woocommerce-pagination ul li a:hover,.woocommerce nav.woocommerce-pagination ul li a:focus{background:#ebe9eb;color:#8a7e8a;}.woocommerce a.button,.woocommerce button.button,.woocommerce input.button,.woocommerce #respond input#submit{color:#515151;background-color:#ebe9eb;}.woocommerce a.button:hover,.woocommerce button.button:hover,.woocommerce input.button:hover,.woocommerce #respond input#submit:hover{background-color:#dad8da;color:#515151;}.woocommerce a.button.alt,.woocommerce button.button.alt,.woocommerce input.button.alt,.woocommerce #respond input#submit.alt{background-color:#2ea3f2;color:#fff;}.woocommerce a.button.alt:hover,.woocommerce button.button.alt:hover,.woocommerce input.button.alt:hover,.woocommerce #respond input#submit.alt:hover{background-color:#1d92e1;color:#fff;}.woocommerce a.button.alt.disabled,.woocommerce button.button.alt.disabled,.woocommerce input.button.alt.disabled,.woocommerce #respond input#submit.alt.disabled,.woocommerce a.button.alt:disabled,.woocommerce button.button.alt:disabled,.woocommerce input.button.alt:disabled,.woocommerce #respond input#submit.alt:disabled,.woocommerce a.button.alt:disabled[disabled],.woocommerce button.button.alt:disabled[disabled],.woocommerce input.button.alt:disabled[disabled],.woocommerce #respond input#submit.alt:disabled[disabled],.woocommerce a.button.alt.disabled:hover,.woocommerce button.button.alt.disabled:hover,.woocommerce input.button.alt.disabled:hover,.woocommerce #respond input#submit.alt.disabled:hover,.woocommerce a.button.alt:disabled:hover,.woocommerce button.button.alt:disabled:hover,.woocommerce input.button.alt:disabled:hover,.woocommerce #respond input#submit.alt:disabled:hover,.woocommerce a.button.alt:disabled[disabled]:hover,.woocommerce button.button.alt:disabled[disabled]:hover,.woocommerce input.button.alt:disabled[disabled]:hover,.woocommerce #respond input#submit.alt:disabled[disabled]:hover{background-color:#2ea3f2;color:#fff;}.woocommerce a.button:disabled:hover,.woocommerce button.button:disabled:hover,.woocommerce input.button:disabled:hover,.woocommerce #respond input#submit:disabled:hover,.woocommerce a.button.disabled:hover,.woocommerce button.button.disabled:hover,.woocommerce input.button.disabled:hover,.woocommerce #respond input#submit.disabled:hover,.woocommerce a.button:disabled[disabled]:hover,.woocommerce button.button:disabled[disabled]:hover,.woocommerce input.button:disabled[disabled]:hover,.woocommerce #respond input#submit:disabled[disabled]:hover{background-color:#ebe9eb;}.woocommerce #reviews h2 small{color:#777;}.woocommerce #reviews h2 small a{color:#777;}.woocommerce #reviews #comments ol.commentlist li .meta{color:#777;}.woocommerce #reviews #comments ol.commentlist li img.avatar{background:#ebe9eb;border:1px solid #e4e1e4;}.woocommerce #reviews #comments ol.commentlist li .comment-text{border:1px solid #e4e1e4;}.woocommerce #reviews #comments ol.commentlist #respond{border:1px solid #e4e1e4;}.woocommerce .star-rating:before{color:#d3ced3;}.woocommerce.widget_shopping_cart .total,.woocommerce .widget_shopping_cart .total{border-top:3px double #ebe9eb;}.woocommerce form.login,.woocommerce form.checkout_coupon,.woocommerce form.register{border:1px solid #d3ced3;}.woocommerce .order_details li{border-right:1px dashed #d3ced3;}.woocommerce .widget_price_filter .ui-slider .ui-slider-handle{background-color:#2ea3f2;}.woocommerce .widget_price_filter .ui-slider .ui-slider-range{background-color:#2ea3f2;}.woocommerce .widget_price_filter .price_slider_wrapper .ui-widget-content{background-color:#005fae;}.woocommerce-cart table.cart td.actions .coupon .input-text{border:1px solid #d3ced3;}.woocommerce-cart .cart-collaterals .cart_totals p small{color:#777;}.woocommerce-cart .cart-collaterals .cart_totals table small{color:#777;}.woocommerce-cart .cart-collaterals .cart_totals .discount td{color:#2ea3f2;}.woocommerce-cart .cart-collaterals .cart_totals tr td,.woocommerce-cart .cart-collaterals .cart_totals tr th{border-top:1px solid #ebe9eb;}.woocommerce-checkout .checkout .create-account small{color:#777;}.woocommerce-checkout #payment{background:#ebe9eb;}.woocommerce-checkout #payment ul.payment_methods{border-bottom:1px solid #d3ced3;}.woocommerce-checkout #payment div.payment_box{background-color:#dfdcdf;color:#515151;}.woocommerce-checkout #payment div.payment_box input.input-text,.woocommerce-checkout #payment div.payment_box textarea{border-color:#c7c1c7;border-top-color:#bab4ba;}.woocommerce-checkout #payment div.payment_box ::-webkit-input-placeholder{color:#bab4ba;}.woocommerce-checkout #payment div.payment_box :-moz-placeholder{color:#bab4ba;}.woocommerce-checkout #payment div.payment_box :-ms-input-placeholder{color:#bab4ba;}.woocommerce-checkout #payment div.payment_box span.help{color:#777;}.woocommerce-checkout #payment div.payment_box:after{content:"";display:block;border:8px solid #dfdcdf;border-right-color:transparent;border-left-color:transparent;border-top-color:transparent;position:absolute;top:-3px;left:0;margin:-1em 0 0 2em;}
</style>
<!--/WooCommerce Colors-->
</head>
<body class="home page-template-default page page-id-5215 woocommerce-no-js et_pb_button_helper_class et_fullwidth_nav et_fixed_nav et_show_nav et_pb_gutter osx et_pb_gutters1 et_primary_nav_dropdown_animation_fade et_secondary_nav_dropdown_animation_fade et_pb_footer_columns_2_3__1_3 et_header_style_left et_pb_pagebuilder_layout et_right_sidebar et_divi_theme et-db et_minified_js et_minified_css">
	<div id="page-container">

	
	
			<header id="main-header" data-height-onload="73">
			<div class="container clearfix et_menu_container">
							<div class="logo_container">
					<span class="logo_helper"></span>
					<a href="https://brinkmanadventures.com/">
						<img src="https://brinkmanadventures.com/wp-content/uploads/2016/10/Brinkman-Logo-Lone-for-black.png" alt="Brinkman Adventures" id="logo" data-height-percentage="54" />
					</a>
				</div>
							<div id="et-top-navigation" data-height="73" data-fixed-height="43">
											<nav id="top-menu-nav">
						<ul id="top-menu" class="nav"><li id="menu-item-5557" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-5215 current_page_item menu-item-5557"><a href="https://brinkmanadventures.com/" aria-current="page">Home</a></li>
<li id="menu-item-9468" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-9468"><a href="https://brinkmanadventures.com/store/audio-dramas">Store</a>
<ul class="sub-menu">
	<li id="menu-item-9467" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-9467"><a href="https://brinkmanadventures.com/store/audio-dramas">Audio Dramas</a></li>
	<li id="menu-item-6715" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6715"><a href="https://brinkmanadventures.com/curriculum-store">Curriculum</a></li>
	<li id="menu-item-6958" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6958"><a href="https://brinkmanadventures.com/store/books">Books</a></li>
	<li id="menu-item-7090" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-7090"><a href="https://brinkmanadventures.com/store/apparel">Apparel</a></li>
</ul>
</li>
<li id="menu-item-94" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94"><a href="https://brinkmanadventures.com/about">About</a></li>
<li id="menu-item-7409" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-7409"><a href="https://brinkmanadventures.com/brinkmanpodcast">Podcast</a></li>
<li id="menu-item-10150" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-10150"><a href="https://brinkmanadventures.com/listen">Listen</a>
<ul class="sub-menu">
	<li id="menu-item-10149" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-10149"><a href="https://brinkmanadventures.com/listen">Episode Previews</a></li>
	<li id="menu-item-8007" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8007"><a href="https://brinkmanadventures.com/radio-stations">Radio Stations</a></li>
</ul>
</li>
<li id="menu-item-98" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-98"><a href="https://brinkmanadventures.com/real-stories">Real Stories</a>
<ul class="sub-menu">
	<li id="menu-item-6814" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6814"><a href="https://brinkmanadventures.com/real-stories/real-stories-season-1">Season 1</a></li>
	<li id="menu-item-6021" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6021"><a href="https://brinkmanadventures.com/real-stories/real-stories-season-2">Season 2</a></li>
	<li id="menu-item-6022" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6022"><a href="https://brinkmanadventures.com/real-stories/real-stories-season-3">Season 3</a></li>
	<li id="menu-item-6023" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6023"><a href="https://brinkmanadventures.com/real-stories/real-stories-season-4">Season 4</a></li>
	<li id="menu-item-6024" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6024"><a href="https://brinkmanadventures.com/real-stories/real-stories-season-5">Season 5</a></li>
	<li id="menu-item-8376" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8376"><a href="https://brinkmanadventures.com/real-stories/real-stories-season-6">Season 6</a></li>
	<li id="menu-item-10485" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-10485"><a href="https://brinkmanadventures.com/real-stories/real-stories-season-7">Season 7</a></li>
</ul>
</li>
<li class="wpmenucartli wpmenucart-display-standard menu-item menu-item-type-post_type menu-item-object-page" id="wpmenucartli"><a class="wpmenucart-contents empty-wpmenucart-visible" href="https://brinkmanadventures.com" title="Start shopping"><i class="wpmenucart-icon-shopping-cart-0"></i><span class="cartcontents">0 items</span></a></li></ul>						</nav>
					
					<a href="https://brinkmanadventures.com/cart" class="et-cart-info">
				<span></span>
			</a>
					
										<div id="et_top_search">
						<span id="et_search_icon"></span>
					</div>
					
					<div id="et_mobile_nav_menu">
				<div class="mobile_nav closed">
					<span class="select_page">Select Page</span>
					<span class="mobile_menu_bar mobile_menu_bar_toggle"></span>
				</div>
			</div>				</div> <!-- #et-top-navigation -->
			</div> <!-- .container -->
			<div class="et_search_outer">
				<div class="container et_search_form_container">
					<form role="search" method="get" class="et-search-form" action="https://brinkmanadventures.com/">
					<input type="search" class="et-search-field" placeholder="Search &hellip;" value="" name="s" title="Search for:" />					</form>
					<span class="et_close_search_field"></span>
				</div>
			</div>
		</header> <!-- #main-header -->
			<div id="et-main-area">
	
<div id="main-content">


			
				<article id="post-5215" class="post-5215 page type-page status-publish hentry">

				
					<div class="entry-content">
					<div id="et-boc" class="et-boc">
			
			<div class="et_builder_inner_content et_pb_gutters1">
				<div class="et_pb_section et_pb_section_0 et_pb_with_background et_section_regular">
				
				
				
				
					<div class="et_pb_row et_pb_row_0 et_pb_row_fullwidth">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_0    et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				<div class="et_pb_module et_pb_image et_pb_image_0 et_pb_image_sticky et_always_center_on_mobile">
				
				
				<a href="https://brinkmanadventures.com/product/brinkman-adventures-season-7"><span class="et_pb_image_wrap "><img src="https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-Available-Now.jpg" alt="" /></span></a>
			</div><div class="et_pb_module et_pb_image et_pb_image_1 et_always_center_on_mobile">
				
				
				<a href="https://brinkmanadventures.com/product/brinkman-adventures-season-7"><span class="et_pb_image_wrap "><img src="https://brinkmanadventures.com/wp-content/uploads/2018/12/Phone-Banner-Available-Now.jpg" alt="" /></span></a>
			</div>
			</div> <!-- .et_pb_column -->
				
				
			</div> <!-- .et_pb_row -->
				
				
			</div> <!-- .et_pb_section --><div id="sneakpeek" class="et_pb_section et_pb_section_1 et_pb_with_background et_pb_section_parallax et_section_regular">
				
				<div class="et_parallax_bg et_pb_parallax_css" style="background-image: url(http://migration.brinkmanadventures.com/wp-content/uploads/2015/08/bg.jpg);"></div>
				
				
					<div class="et_pb_row et_pb_row_1 et_pb_row_fullwidth">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_1    et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_0 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h1 style="text-align: center;"><strong><span style="font-size: 36pt;">About</span></strong></h1>
<p style="text-align: left;"><span style="font-size: 14pt; color: #000000;">What happens when you take the wacky adventures of a big family and mix them with exciting true stories of modern day Christian heroes?  You get a captivating audio drama series called <b>The Brinkman Adventures</b>!  Powerful stories from the lives of real missionaries come to life through the humorous escapades of the Brinkman family.  These adventures will strengthen your faith and family and inspire young and old to follow Jesus wherever He may lead. <b>The Brinkman Adventures</b> are a treat for the ears, mind, and heart.  So sit back, turn up the volume, and get ready…</span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p style="text-align: center;"> </p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_1 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<p style="text-align: left;"><em>Brinkman Adventures is an exciting radio show that tells true, modern, missionary stories through the eyes of the fictional Brinkman family. The series is produced by <a href="http://beachglassministries.org/" target="_blank" rel="noopener">Beachglass Ministries</a>, a non-profit, non-denominational Christian organization dedicated to inspiring, motivating and facilitating the next generation of Christian world changers.  </em></p>
<p style="text-align: left;"><em>CD &amp; download sales cover only a portion of the expenses associated with bringing you these stories.  If your family has benefited from Brinkman Adventures, please consider supporting us financially and helping us continue producing quality entertainment that inspires, teaches and glorifies God.</em></p>
<form class="alignright" action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top"><input name="cmd" type="hidden" value="_s-xclick" /><br />
<input style="cursor: pointer;" name="hosted_button_id" type="hidden" value="M7CJ3A8FD4C6L" /><br />
<input style="cursor: pointer;" alt="PayPal - The safer, easier way to pay online!" name="submit" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" type="image" /><br />
<img src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" alt="" width="1" height="1" border="0" /></form>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column -->
				
				
			</div> <!-- .et_pb_row --><div class="et_pb_row et_pb_row_2 et_animated et_pb_gutters4 et_pb_row_fullwidth">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_2    et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_2 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<hr />
<p>&nbsp;</p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column -->
				
				
			</div> <!-- .et_pb_row --><div class="et_pb_row et_pb_row_3 et_animated et_pb_gutters4 et_pb_row_fullwidth">
				<div class="et_pb_column et_pb_column_1_2 et_pb_column_3    et_pb_css_mix_blend_mode_passthrough">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_3 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-1"><img class="season_image alignleft wp-image-4692" src="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-150x150.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-1"><br />
Season 1</a><br />
</span></h2>
<p style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes<br />
</span></span>What happens when you take the wacky adventures of a big family and mix them with exciting true stories of modern day Christian heroes?  You get a brand new audio drama series called <b>The Brinkman Adventures</b>!  Powerful stories from the lives of real missionaries come to life through the humorous escapades of the Brinkman family.  These adventures will strengthen your faith and family and inspire young and old to follow Jesus wherever He may lead.  <b>The Brinkman Adventures</b> are a treat for the ears, mind, and heart.  So sit back, turn up the volume, and get ready</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_4 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-3-2"><img class="season_image alignleft wp-image-4690" src="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
<a href="https://brinkmanadventures.com/product/season-3"> Season 3</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes</span></span></p>
<p style="text-align: left;">The Brinkman family returns for another exciting season of missionary stories and family adventures.  From dangerous terrorists and a Taliban jail to threatening wolves and hypothermia, new challenges push our characters to the limit of endurance and force them to face their deepest fears.  Travel the globe from Ecuador to Kashmir and from Africa to Alaska as you listen to these amazing stories and discover God’s wonderful truths.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_5 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/brinkman-adventures-season-5"><img class="season_image alignleft wp-image-4688" src="https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
Season 5<br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">6 Episodes</span></span></p>
<p style="text-align: left;">The Tanzanian mafia gets more than it bargained for when it captures Michelle and Anthony during their honeymoon in Africa.  Back home, Mr. Pennington helps Ian upgrade his robot only to have it escape and follow the family across the country as they head for the Badlands.   Later, the Brinkman kids learn some unforgettable lessons about missions while on a trip to an Alaskan village.   These six well-crafted episodes will stir the imagination and inspire the soul.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_6 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/brinkman-adventures-season-7"><img class="season_image alignleft wp-image-10146" src="https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2018/12/Season-7-sq-itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />Season 7<br /></span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">6 Episodes</span></span></p>
<p style="text-align: left;">Join Dave Eubank and his Free Burma Rangers as they rescue survivors hiding in the war-torn city of Mosul, Iraq. Then follow the Brinkman kids as they search for a thief and saboteur while learning important life lessons. Season 7 of the Brinkman Adventures continues to deliver off-the-chart excitement, laughter, and life-changing drama.</p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column --><div class="et_pb_column et_pb_column_1_2 et_pb_column_4    et_pb_css_mix_blend_mode_passthrough">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_7 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-2"><img class="season_image alignleft wp-image-4691" src="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
<a href="https://brinkmanadventures.com/product/season-2">Season 2</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes</span></span></p>
<p style="text-align: left;">The Brinkmans are back with 12 brand new heart-pounding, edge of your seat adventures. When Ian discovers a golden ring at the bottom of Random Lake, the family embarks on a quest for the ring’s owner and gets more than they bargained for.  These exciting episodes take you on a globe-trotting, adrenaline filled journey while telling modern day missionary stories through the lives of the crazy Brinkman family.  Join them as they battle unscrupulous slave owners, flee from Mexican bandits and search for hidden pirate treasure on an ancient Mayan island.  If you’re looking for ‘must listen to’ audio drama,<i> Season Two</i> of <b>The Brinkman Adventures</b> more than delivers!</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_8 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/brinkman-adventures-season-4"><img class="season_image alignleft wp-image-8519" src="https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2017/12/1-02-038_-Remember-Nhu-mp3-image.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
<a href="https://brinkmanadventures.com/product/season-4">Season 4</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes</span></span></p>
<p style="text-align: left;">Season Four of the Brinkman Adventures takes you from houseboats in Cambodia to frozen prisons in Russia and dangerous alleys in the Middle East.  While dodging angry hippos and taming rogue robots, the Brinkmans will introduce you to Christian heroes who will strengthen your faith and provide important teachable moments.  Enjoy over five hours of high definition, heart-stopping audio-drama in the latest offering from the award-winning series.  Inspired by the lives of Dr. Nik Ripken, Carl Ralston, and others, this volume will be cherished and listened to for years to come.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_9 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/brinkman-adventures-season-6"><img class="season_image alignleft wp-image-7941" src="https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-1024x1024.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
Season 6<br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">6 Episodes</span></span></p>
<p style="text-align: left;">Press play, fasten your seatbelts and hang on as you step back in time to war-torn Holland. The Brinkmans’ great-grandparents must choose between protecting themselves from the Nazis, or aiding the Jews in this riveting tale based on real-life events. Then Jack &amp; Ian join Dave Eubank and his Free Burma Rangers in a daring mission to save a Burmese village from a pursuing army bent on destruction. Season 6 continues in the tradition of high octane, faith growing stories.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_10 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/curriculum-store"><img class="season_image alignleft wp-image-6883" src="https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only.jpg 972w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-768x768.jpg 768w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/curriculum-store"><br />
Living The Call Curriculum</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 lessons</span></span></p>
<p style="text-align: left;">Living the Call is a mission-themed curriculum that introduces your students to modern-day missionaries through 12 heart-pounding, edge-of-your-seat audio adventures. Students will learn about storing up treasure in heaven, the power of the Gospel, pushing past fear, overcoming evil with good, honoring their parents, loving their siblings, seeing with gratitude and much more as they discover how to shine as lights in the world around them.</p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column -->
				
				
			</div> <!-- .et_pb_row --><div class="et_pb_row et_pb_row_4 et_pb_gutters4 et_pb_row_fullwidth">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_5    et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_11 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-1"><img class="aligncenter wp-image-4692" src="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-150x150.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season1itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-1"><br />
Season 1</a><br />
</span></h2>
<p style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes</span></span></p>
<p style="text-align: left;">What happens when you take the wacky adventures of a big family and mix them with exciting true stories of modern day Christian heroes?  You get a brand new audio drama series called <b>The Brinkman Adventures</b>!  Powerful stories from the lives of real missionaries come to life through the humorous escapades of the Brinkman family.  These adventures will strengthen your faith and family and inspire young and old to follow Jesus wherever He may lead.  <b>The Brinkman Adventures</b> are a treat for the ears, mind, and heart.  So sit back, turn up the volume, and get ready</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_12 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-2"><img class="aligncenter wp-image-4691" src="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-300x300.jpg" alt="" width="210" height="210" srcset="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season2itunes.jpg 1500w" sizes="(max-width: 210px) 100vw, 210px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
<a href="https://brinkmanadventures.com/product/season-2">Season 2</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes</span></span></p>
<p style="text-align: left;">The Brinkmans are back with 12 brand new heart-pounding, edge of your seat adventures. When Ian discovers a golden ring at the bottom of Random Lake, the family embarks on a quest for the ring’s owner and gets more than they bargained for.  These exciting episodes take you on a globe-trotting, adrenaline filled journey while telling modern day missionary stories through the lives of the crazy Brinkman family.  Join them as they battle unscrupulous slave owners, flee from Mexican bandits and search for hidden pirate treasure on an ancient Mayan island.  If you’re looking for ‘must listen to’ audio drama,<i> Season Two</i> of <b>The Brinkman Adventures</b> more than delivers!</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_13 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/season-3-2"><img class="aligncenter wp-image-4690" src="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2015/08/Season3itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
<a href="https://brinkmanadventures.com/product/season-3"> Season 3</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes</span></span></p>
<p style="text-align: left;">The Brinkman family returns for another exciting season of missionary stories and family adventures.  From dangerous terrorists and a Taliban jail to threatening wolves and hypothermia, new challenges push our characters to the limit of endurance and force them to face their deepest fears.  Travel the globe from Ecuador to Kashmir and from Africa to Alaska as you listen to these amazing stories and discover God’s wonderful truths.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_14 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/brinkman-adventures-season-4"><img class="aligncenter wp-image-4689" src="https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-300x300.jpg" alt="" width="210" height="210" srcset="https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2015/12/Season4itunes.jpg 1500w" sizes="(max-width: 210px) 100vw, 210px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
<a href="https://brinkmanadventures.com/product/season-4">Season 4</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 Episodes</span></span></p>
<p style="text-align: left;">Season Four of the Brinkman Adventures takes you from houseboats in Cambodia to frozen prisons in Russia and dangerous alleys in the Middle East.  While dodging angry hippos and taming rogue robots, the Brinkmans will introduce you to Christian heroes who will strengthen your faith and provide important teachable moments.  Enjoy over five hours of high definition, heart-stopping audio-drama in the latest offering from the award-winning series.  Inspired by the lives of Dr. Nik Ripken, Carl Ralston, and others, this volume will be cherished and listened to for years to come.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_15 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/brinkman-adventures-season-5"><img class="wp-image-4688 aligncenter" src="https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2016/12/Season-5-itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
Season 5<br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">6 Episodes</span></span></p>
<p style="text-align: left;">The Tanzanian mafia gets more than it bargained for when it captures Michelle and Anthony during their honeymoon in Africa.  Back home, Mr. Pennington helps Ian upgrade his robot only to have it escape and follow the family across the country as they head for the Badlands.   Later, the Brinkman kids learn some unforgettable lessons about missions while on a trip to an Alaskan village.   These six well-crafted episodes will stir the imagination and inspire the soul.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_16 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/product/brinkman-adventures-season-6"><img class="aligncenter wp-image-7941" src="https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-300x300.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-768x768.jpg 768w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-1024x1024.jpg 1024w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-1080x1080.jpg 1080w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2017/11/Season-6-sq-itunes.jpg 1500w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><br />
Season 6<br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">6 Episodes</span></span></p>
<p style="text-align: left;">Press play, fasten your seatbelts and hang on as you step back in time to war-torn Holland. The Brinkmans’ great-grandparents must choose between protecting themselves from the Nazis, or aiding the Jews in this riveting tale based on real-life events. Then Jack &amp; Ian join Dave Eubank and his Free Burma Rangers in a daring mission to save a Burmese village from a pursuing army bent on destruction. Season 6 continues in the tradition of high octane, faith growing stories.</p>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_17 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h2 style="text-align: left;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/curriculum-store"><img class="wp-image-6883 aligncenter" src="https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only.jpg" alt="" width="208" height="208" srcset="https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only.jpg 972w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-30x30.jpg 30w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-350x350.jpg 350w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-400x400.jpg 400w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-510x510.jpg 510w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-100x100.jpg 100w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-150x150.jpg 150w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-300x300.jpg 300w, https://brinkmanadventures.com/wp-content/uploads/2017/09/Teacher-Manuel-Only-768x768.jpg 768w" sizes="(max-width: 208px) 100vw, 208px" /></a></span></h2>
<hr />
<h2 style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><a href="https://brinkmanadventures.com/curriculum-store"><br />
Living The Call Curriculum</a><br />
</span></h2>
<p style="text-align: left; margin-bottom: 0px; padding-bottom: 0;"><span style="font-family: 'book antiqua', palatino, serif;"><span style="font-size: 10pt; color: #333333; margin-top: 0; padding-top: 0;">12 lessons</span></span></p>
<p style="text-align: left;">Living the Call is a mission-themed curriculum that introduces your students to modern-day missionaries through 12 heart-pounding, edge-of-your-seat audio adventures. Students will learn about storing up treasure in heaven, the power of the Gospel, pushing past fear, overcoming evil with good, honoring their parents, loving their siblings, seeing with gratitude and much more as they discover how to shine as lights in the world around them.</p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column -->
				
				
			</div> <!-- .et_pb_row -->
				
				
			</div> <!-- .et_pb_section -->			</div>
			
		</div>					</div> <!-- .entry-content -->

				
				</article> <!-- .et_pb_post -->

			

</div> <!-- #main-content -->


			<div id="footer" class="sb_dli_pre_footer et_pb_section  et_pb_section_4 et_pb_with_background et_section_regular">
				
				
				
				
					<div class="et_pb_row et_pb_row_5 et_pb_gutters2">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_6    et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_18 socialIcons et_pb_bg_layout_light  et_pb_text_align_center">
				
				
				<div class="et_pb_text_inner">
					<p><a href="https://www.facebook.com/BrinkmanAdventures" target="_blank" rel="noopener"><img class="alignnone wp-image-2150 size-full" style="margin-right: 8%; margin-bottom: 1%;" src="https://brinkmanadventures.com/wp-content/uploads/2017/10/011.png" alt="01" width="15" height="27"></a><a href="https://twitter.com/Brinkman_Tweets?lang=en" target="_blank" rel="noopener"><img class="alignnone wp-image-2151 size-medium" style="margin-right: 8%; margin-bottom: 1%;" src="https://brinkmanadventures.com/wp-content/uploads/2017/10/021.png" alt="02" width="34" height="27"></a><a href="https://www.instagram.com/brinkmanadventures/?hl=en" target="_blank" rel="noopener"><img class="alignnone wp-image-2152 size-medium" style="margin-right: 8%; margin-bottom: 1%;" src="https://brinkmanadventures.com/wp-content/uploads/2017/10/031.png" alt="03" width="27" height="27"></a><a href="https://www.youtube.com/user/BrinkmanAdventures" target="_blank" rel="noopener"><img class="alignnone wp-image-2154 size-medium" style="margin-right: 8%; margin-bottom: 1%;" src="https://brinkmanadventures.com/wp-content/uploads/2017/10/05.png" alt="05" width="33" height="25"></a><a href="https://brinkmanadventures.com/feed/podcast" target="_blank" rel="noopener"><img class="alignnone wp-image-2154 size-medium" style="margin-right: 8%; margin-bottom: 1%;" src="https://brinkmanadventures.com/wp-content/uploads/2017/10/08.png" alt="05" width="27" height="27"></a></p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column -->
				
				
			</div> <!-- .et_pb_row -->
				
				
			</div> <!-- .et_pb_section --><div class="sb_dli_pre_footer et_pb_section  et_pb_section_5 et_pb_with_background et_section_regular">
				
				
				
				
					<div class="et_pb_row et_pb_row_6 et_pb_gutters2">
				<div class="et_pb_column et_pb_column_1_2 et_pb_column_7    et_pb_css_mix_blend_mode_passthrough">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_19 et_pb_bg_layout_dark  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h1><strong>Why Donate?</strong></h1>
<p>Your gifts allow us to continue producing quality content. Brinkman Adventures is produced by Beachglass Ministries, a 501 c(3) non-profit organization dedicated to "inspiring the next generation of Christian World Changers." </p>
<p>&nbsp;</p>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top"><input name="cmd" type="hidden" value="_s-xclick" /> <input name="hosted_button_id" type="hidden" value="M7CJ3A8FD4C6L" /> <input alt="PayPal - The safer, easier way to pay online!" name="submit" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" type="image" /> <img src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" alt="" width="1" height="1" border="0" /></form>
				</div>
			</div> <!-- .et_pb_text --><div class="et_pb_module et_pb_text et_pb_text_20 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<p style="text-align: left; padding-left: 30px;">© 2018 Brinkman Adventures.</p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column --><div class="et_pb_column et_pb_column_1_4 et_pb_column_8    et_pb_css_mix_blend_mode_passthrough">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_21 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h1><strong>Explore</strong></h1>
<p><span style="color: #ffffff;"><a href="https://brinkmanadventures.com/">Home</a></span><br />
 <span style="color: #ffffff;"> <a href="https://brinkmanadventures.com/about">About</a></span><br />
 <span style="color: #ffffff;"> <a href="https://brinkmanadventures.com/listen">Listen</a></span><br />
 <span style="color: #ffffff;"> <a href="http://blog.brinkmanadventures.com">Blog</a></span><br />
 <span style="color: #ffffff;"><a href="https://brinkmanadventures.com/fun-stuff">Fun Stuff</a></span><br />
 <span style="color: #ffffff;"> <a href="https://brinkmanadventures.com/links">Other Audio Dramas</a> </span><br />
 <span style="color: #ffffff;"> <a href="https://brinkmanadventures.com/contact">Contact Us</a></span><br />
<span style="color: #ffffff;"> <a href="https://brinkmanadventures.com/donate">Donate</a></span></p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column --><div class="et_pb_column et_pb_column_1_4 et_pb_column_9    et_pb_css_mix_blend_mode_passthrough">
				
				
				<div class="et_pb_module et_pb_text et_pb_text_22 et_pb_bg_layout_light  et_pb_text_align_left">
				
				
				<div class="et_pb_text_inner">
					<h1><strong>Our Store</strong></h1>
<p><span style="color: #ffffff;"><a href="https://brinkmanadventures.com/store/audio-dramas">Audio Dramas</a></span><br />
 <span style="color: #ffffff;"> <a href="https://brinkmanadventures.com/curriculum-store">Curriculum</a></span><br />
 <span style="color: #ffffff;"> <a href="https://brinkmanadventures.com/store/books">Books<br />
 </a></span><span style="color: #ffffff;"><a href="https://brinkmanadventures.com/store/apparel">Apparel</a></span></p>
				</div>
			</div> <!-- .et_pb_text -->
			</div> <!-- .et_pb_column -->
				
				
			</div> <!-- .et_pb_row -->
				
				
			</div> <!-- .et_pb_section --><footer id="main-footer">
                                <div class="et_pb_section et_pb_section_2 et_section_regular">
				
				
				
				
					
				
				
			</div> <!-- .et_pb_section -->				

		
				<div id="et-footer-nav">
					<div class="container">
						<ul id="menu-footer-menu" class="bottom-nav"><li id="menu-item-5556" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-5215 current_page_item menu-item-5556"><a href="https://brinkmanadventures.com/" aria-current="page">Home</a></li>
<li id="menu-item-2821" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2821"><a href="http://blog.brinkmanadventures.com">Blog</a></li>
<li id="menu-item-555" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-555"><a href="https://brinkmanadventures.com/about">About</a></li>
<li id="menu-item-4827" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-4827"><a href="https://brinkmanadventures.com/store">Store</a></li>
<li id="menu-item-559" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-559"><a href="https://brinkmanadventures.com/real-stories">Real Stories</a></li>
<li id="menu-item-556" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-556"><a href="https://brinkmanadventures.com/contact">Contact</a></li>
<li id="menu-item-557" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-557"><a href="https://brinkmanadventures.com/fun-stuff">Fun Stuff</a></li>
<li id="menu-item-5158" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5158"><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&#038;hosted_button_id=YQT6RNS6G5T9Q">Donate</a></li>
<li id="menu-item-5831" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5831"><a href="https://brinkmanadventures.com/links">Links</a></li>
</ul>					</div>
				</div> <!-- #et-footer-nav -->

			
				<div id="footer-bottom">
					<div class="container clearfix">
				<ul class="et-social-icons">

	<li class="et-social-icon et-social-facebook">
		<a href="https://www.facebook.com/Brinkman-Adventures-152895116079/" class="icon">
			<span>Facebook</span>
		</a>
	</li>
	<li class="et-social-icon et-social-twitter">
		<a href="https://twitter.com/Brinkman_Tweets" class="icon">
			<span>Twitter</span>
		</a>
	</li>

</ul><p id="footer-info">Designed by <a href="http://www.elegantthemes.com" title="Premium WordPress Themes">Elegant Themes</a> | Powered by <a href="http://www.wordpress.org">WordPress</a></p>					</div>	<!-- .container -->
				</div>
			</footer> <!-- #main-footer -->
		</div> <!-- #et-main-area -->


	</div> <!-- #page-container -->

	
<div class="xoo-cp-opac"></div>
<div class="xoo-cp-modal">
	<div class="xoo-cp-container">
		<div class="xoo-cp-outer">
			<div class="xoo-cp-cont-opac"></div>
			<span class="xoo-cp-preloader xoo-cp-icon-spinner"></span>
		</div>
		<span class="xoo-cp-close xoo-cp-icon-cross"></span>

		<div class="xoo-cp-content"></div>
			
			
		<div class="xoo-cp-btns">
			<a class="xoo-cp-btn-vc xcp-btn" href="https://brinkmanadventures.com/cart">View Cart</a>
			<a class="xoo-cp-btn-ch xcp-btn" href="https://brinkmanadventures.com/checkout">Checkout</a>
			<a class="xoo-cp-close xcp-btn">Continue Shopping</a>
		</div>
			</div>
</div>


<div class="xoo-cp-notice-box" style="display: none;">
	<div>
	  <span class="xoo-cp-notice"></span>
	</div>
</div>
	<script type="text/javascript">
				var et_animation_data = [{"class":"et_pb_row_2","style":"slideLeft","repeat":"once","duration":"750ms","delay":"0ms","intensity":"29%","starting_opacity":"0%","speed_curve":"ease-in-out"},{"class":"et_pb_row_3","style":"slideBottom","repeat":"once","duration":"850ms","delay":"0ms","intensity":"8%","starting_opacity":"0%","speed_curve":"ease-in-out"}];
			</script>
		<script type="text/javascript">
		var c = document.body.className;
		c = c.replace(/woocommerce-no-js/, 'woocommerce-js');
		document.body.className = c;
	</script>
	<script>// <![CDATA[
var th = jQuery('#top-header').height(); var hh = jQuery('#main-header').height(); var fh = jQuery('#main-footer').height(); var wh = jQuery(window).height(); var ch = wh - (th + hh + fh); jQuery('#main-content').css('min-height', ch);
// ]]></script>

<style type="text/css">
#main-header .et_mobile_menu .menu-item-has-children > a { background-color: transparent; position: relative; }
#main-header .et_mobile_menu .menu-item-has-children > a:after { font-family: 'ETmodules'; text-align: center; speak: none; font-weight: normal; font-variant: normal; text-transform: none; -webkit-font-smoothing: antialiased; position: absolute; }
#main-header .et_mobile_menu .menu-item-has-children > a:after { font-size: 16px; content: '\4c'; top: 13px; right: 10px; }
#main-header .et_mobile_menu .menu-item-has-children.visible > a:after { content: '\4d'; }
#main-header .et_mobile_menu ul.sub-menu { display: none !important; visibility: hidden !important;  transition: all 1.5s ease-in-out;}
#main-header .et_mobile_menu .visible > ul.sub-menu { display: block !important; visibility: visible !important; }
</style>

<script type="text/javascript">
(function($) {
      
    function setup_collapsible_submenus() {
        var $menu = $('#mobile_menu'),
            top_level_link = '#mobile_menu .menu-item-has-children > a';
             
        $menu.find('a').each(function() {
            $(this).off('click');
              
            if ( $(this).is(top_level_link) ) {
                $(this).attr('href', '#');
            }
              
            if ( ! $(this).siblings('.sub-menu').length ) {
                $(this).on('click', function(event) {
                    $(this).parents('.mobile_nav').trigger('click');
                });
            } else {
                $(this).on('click', function(event) {
                    event.preventDefault();
                    $(this).parent().toggleClass('visible');
                });
            }
        });
    }
      
    $(window).load(function() {
        setTimeout(function() {
            setup_collapsible_submenus();
        }, 700);
    });
 
})(jQuery);
</script>

<script type="text/javascript">
jQuery(function() {
      if(jQuery("body").hasClass("single-product")){
         
        if(jQuery(".entry-summary").parent().hasClass("product_cat-qurytewoiueyt")){
          jQuery(document.body).addClass("apparel");
      }
         
         else if(jQuery(".entry-summary").parent().hasClass("product_cat-kjhgiuakhjdkfj")){
           jQuery(document.body).addClass("books");
      }
         
         else if(jQuery(".entry-summary").parent().hasClass("product_cat-asdgsdgjffbdhreasfs")){
          jQuery(document.body).addClass("audioDrama");
         }

         if(jQuery("body").hasClass("audioDrama")){
          jQuery(".xoo-cp-close").attr("href", "https://brinkmanadventures.com/store/audio-dramas")
      }
         
         else if(jQuery("body").hasClass("books")){
          jQuery(".xoo-cp-close").attr("href", "https://brinkmanadventures.com/store/books")
      }
         
         else if(jQuery("body").hasClass("apparel")){
          jQuery(".xoo-cp-close").attr("href", "https://brinkmanadventures.com/store/apparel")
      }
  }
})
</script>


<link rel='stylesheet' id='so-css-Divi-css'  href='https://brinkmanadventures.com/wp-content/uploads/so-css/so-css-Divi.css?ver=1544477855' type='text/css' media='all' />
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/js/jquery-blockui/jquery.blockUI.min.js?ver=2.70'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var wc_add_to_cart_params = {"ajax_url":"\/wp-admin\/admin-ajax.php","wc_ajax_url":"\/?wc-ajax=%%endpoint%%","i18n_view_cart":"View cart","cart_url":"https:\/\/brinkmanadventures.com\/cart","is_cart":"","cart_redirect_after_add":"no"};
/* ]]> */
</script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/js/frontend/add-to-cart.min.js?ver=3.5.5'></script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/js/js-cookie/js.cookie.min.js?ver=2.1.4'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var woocommerce_params = {"ajax_url":"\/wp-admin\/admin-ajax.php","wc_ajax_url":"\/?wc-ajax=%%endpoint%%"};
/* ]]> */
</script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/js/frontend/woocommerce.min.js?ver=3.5.5'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var wc_cart_fragments_params = {"ajax_url":"\/wp-admin\/admin-ajax.php","wc_ajax_url":"\/?wc-ajax=%%endpoint%%","cart_hash_key":"wc_cart_hash_630410291db761edf2872bc121a326f0","fragment_name":"wc_fragments_630410291db761edf2872bc121a326f0"};
/* ]]> */
</script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/woocommerce/assets/js/frontend/cart-fragments.min.js?ver=3.5.5'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var xoo_cp_localize = {"adminurl":"https:\/\/brinkmanadventures.com\/wp-admin\/admin-ajax.php","homeurl":"https:\/\/brinkmanadventures.com","wc_ajax_url":"\/?wc-ajax=%%endpoint%%","reset_cart":""};
/* ]]> */
</script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/added-to-cart-popup-woocommerce/assets/js/xoo-cp-js.min.js?ver=1.4'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var DIVI = {"item_count":"%d Item","items_count":"%d Items"};
var et_shortcodes_strings = {"previous":"Previous","next":"Next"};
var et_pb_custom = {"ajaxurl":"https:\/\/brinkmanadventures.com\/wp-admin\/admin-ajax.php","images_uri":"https:\/\/brinkmanadventures.com\/wp-content\/themes\/Divi\/images","builder_images_uri":"https:\/\/brinkmanadventures.com\/wp-content\/themes\/Divi\/includes\/builder\/images","et_frontend_nonce":"986f53893b","subscription_failed":"Please, check the fields below to make sure you entered the correct information.","et_ab_log_nonce":"fb16807a53","fill_message":"Please, fill in the following fields:","contact_error_message":"Please, fix the following errors:","invalid":"Invalid email","captcha":"Captcha","prev":"Prev","previous":"Previous","next":"Next","wrong_captcha":"You entered the wrong number in captcha.","ignore_waypoints":"no","is_divi_theme_used":"1","widget_search_selector":".widget_search","is_ab_testing_active":"","page_id":"5215","unique_test_id":"","ab_bounce_rate":"5","is_cache_plugin_active":"no","is_shortcode_tracking":"","tinymce_uri":""};
var et_pb_box_shadow_elements = [];
/* ]]> */
</script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/themes/Divi/js/custom.min.js?ver=3.19.15'></script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/variation-swatches-for-woocommerce/assets/js/frontend.js?ver=20160615'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var BJLL_options = {"threshold":"50"};
/* ]]> */
</script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/plugins/bj-lazy-load/js/bj-lazy-load.min.js?ver=2'></script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-content/themes/Divi/core/admin/js/common.js?ver=3.19.15'></script>
<script type='text/javascript' src='https://brinkmanadventures.com/wp-includes/js/wp-embed.min.js?ver=5.1'></script>
<style id="et-builder-module-design-cached-inline-styles">div.et_pb_section.et_pb_section_0{background-image:url(http://migration.brinkmanadventures.com/wp-content/uploads/2015/08/bg.jpg)!important}.et_pb_row_6.et_pb_row{padding-top:50px;padding-bottom:50px}.et_pb_text_16{padding-top:5px!important;padding-bottom:20px!important;margin-bottom:8.696%!important;margin-bottom:8.696%!important}.et_pb_text_17 h1{line-height:1.7em}.et_pb_text_17{padding-bottom:20px!important;margin-bottom:8.696%!important;margin-bottom:8.696%!important}.et_pb_section_3{padding-top:0px;padding-bottom:0px;z-index:10;box-shadow:0px -7px 19px -6px rgba(0,0,0,0.3)}.et_pb_section_4{padding-top:0px;padding-bottom:0px;z-index:10;box-shadow:0px -7px 19px -6px rgba(0,0,0,0.3);-webkit-transition:all 0.3s ease;transition:all 0.3s ease}.et_pb_section_4.et_pb_section{background-color:#ffffff!important}.et_pb_row_5.et_pb_row{padding-top:1%}.et_pb_text_18 p{line-height:1em}.et_pb_text_18{line-height:1em}.et_pb_section_5.et_pb_section{background-color:#444444!important}.et_pb_text_19.et_pb_text{color:#ffffff!important}.et_pb_section_0{z-index:10;box-shadow:0px 7px 25px -6px rgba(0,0,0,0.3)}.et_pb_text_19 p{line-height:1.5em}.et_pb_text_19{font-family:'Source Sans Pro',Helvetica,Arial,Lucida,sans-serif;font-size:16px;line-height:1.5em;max-width:300px;padding-right:5%!important;padding-left:5%!important;margin-bottom:5px!important}.et_pb_text_19 h1{font-size:22px;color:#b3b3b3!important}.et_pb_text_20.et_pb_text{color:#aaaaaa!important}.et_pb_text_20 p{line-height:1.5em}.et_pb_text_20{font-family:'Source Sans Pro',Helvetica,Arial,Lucida,sans-serif;font-size:12px;line-height:1.5em;max-width:300px;padding-top:0px!important}.et_pb_text_21.et_pb_text{color:#ffffff!important}.et_pb_text_21{font-family:'Source Sans Pro',Helvetica,Arial,Lucida,sans-serif;font-size:18px}.et_pb_text_21 h1{font-size:22px;color:#b3b3b3!important}.et_pb_text_22.et_pb_text{color:#ffffff!important}.et_pb_text_22{font-family:'Source Sans Pro',Helvetica,Arial,Lucida,sans-serif;font-size:18px;padding-right:5%!important}.et_pb_text_15{padding-top:5px!important;padding-bottom:20px!important;margin-bottom:8.696%!important;margin-bottom:8.696%!important}.et_pb_text_14{padding-bottom:100px!important;margin-bottom:2%!important}.et_pb_text_13{padding-bottom:100px!important;margin-bottom:8.696%!important}.et_pb_text_12{padding-bottom:79px!important;margin-bottom:8.696%!important}.et_pb_section_0.et_pb_section{background-color:#fcfcfc!important}.et_pb_image_0{position:relative;top:0;max-width:100%!important;text-align:center}.et_pb_image_0 .et_pb_image_wrap,.et_pb_image_0 img{width:100%}.et_pb_image_1{max-width:100%!important;text-align:center}.et_pb_image_1 .et_pb_image_wrap,.et_pb_image_1 img{width:100%}.et_pb_section_1:before{@media all and (min-width:11in){body{zoom:1.5}}}.et_pb_section_1.et_pb_section{background-color:#ffffff!important}.et_pb_row_1.et_pb_row{margin-top:2%!important;margin-bottom:5%!important;padding-right:5%;padding-left:5%}.et_pb_text_1.et_pb_text{color:#000000!important}.et_pb_text_1{font-size:18px;.pointerhand{cursor:pointer}}.et_pb_row_2.et_pb_row{margin-top:3%!important;padding-right:5%;padding-left:5%}.et_pb_row_3.et_pb_row{margin-top:5%!important;margin-bottom:2%!important}.et_pb_text_3{padding-bottom:100px!important;margin-bottom:8%!important;margin-bottom:10%!important;height:370px}.et_pb_text_4{padding-bottom:100px!important;margin-bottom:10%!important;height:370px}.et_pb_text_5{padding-top:5px!important;padding-bottom:20px!important;margin-bottom:8.696%!important;margin-bottom:10%!important;height:370px}.et_pb_text_6{padding-top:5px!important;padding-bottom:20px!important;margin-bottom:8.696%!important;margin-bottom:10%!important;height:370px}.et_pb_text_7{padding-bottom:79px!important;margin-bottom:8%!important;margin-bottom:10%!important;height:370px}.et_pb_text_8{padding-bottom:100px!important;margin-bottom:10%!important;height:370px}.et_pb_text_9{padding-top:5px!important;padding-bottom:20px!important;margin-bottom:8.696%!important;margin-bottom:10%!important;height:370px}.et_pb_text_10 h1{line-height:1.7em}.et_pb_text_10{padding-bottom:20px!important;margin-bottom:8.696%!important;margin-bottom:8.696%!important;height:370px}.et_pb_row_4.et_pb_row{margin-top:5%!important;margin-bottom:5%!important;padding-right:10%;padding-left:10%}.et_pb_text_11{padding-bottom:100px!important;margin-bottom:8.696%!important}.et_pb_text_22 h1{font-size:22px;color:#b3b3b3!important}.et_pb_text_19.et_pb_module{margin-left:0px!important;margin-right:auto!important}.et_pb_text_20.et_pb_module{margin-left:0px!important;margin-right:auto!important}@media only screen and (min-width:981px){.et_pb_image_1{display:none!important}.et_pb_row_3.et_pb_row{padding-right:5%;padding-left:5%}.et_pb_row_4{display:none!important}}@media only screen and (max-width:980px){.et_pb_section_0{padding-top:50px;padding-right:0px;padding-bottom:50px;padding-left:0px;margin-top:0px}.et_pb_section_1{padding-top:50px;padding-right:0px;padding-bottom:50px;padding-left:0px}.et_pb_row_1.et_pb_row{padding-right:10%!important;padding-left:10%!important}.et_pb_row_2.et_pb_row{padding-right:10%!important;padding-left:10%!important}.et_pb_row_5.et_pb_row{padding-top:1%!important;padding-bottom:1%!important}.et_pb_text_19{margin-bottom:10px!important}}@media only screen and (min-width:768px) and (max-width:980px){.et_pb_image_1{display:none!important}.et_pb_row_4{display:none!important}}@media only screen and (max-width:767px){.et_pb_image_0{display:none!important}.et_pb_row_3{display:none!important}}</style>		<script type="text/javascript">
			var bwpRecaptchaCallback = function() {
				// render all collected recaptcha instances
			};
		</script>

		<script src="https://www.google.com/recaptcha/api.js?onload=bwpRecaptchaCallback&#038;render=explicit" async defer></script>
</body>
</html>
"""
        self.rules = [[[Rules.TagIs(does=True, condition='a'), Rules.HasAttribute(does=True, condition='class')],
                       [Rules.Contains(does=True, condition='hey'),
                        Rules.HasAttributeThatIs(does=True, condition='class', attribute_value='test_class')]],
                      [[Rules.HasAttribute(does=True, condition='href')]]]

    def test_tag_matches_or_group(self):
        html = '<a href="https://www.facebook.com/Brinkman-Adventures-152895116079/" class="icon">Facebook</a>' \
               '<div class="icon">Facebook</div>'
        soup = bs4.BeautifulSoup(html, 'html.parser')
        rules = self.rules[0][0]
        self.assertEqual(self.converter.test_if_tag_matches_or_group(rules, soup.find('a')), True)
        self.assertEqual(self.converter.test_if_tag_matches_or_group(rules, soup.find('div')), False)

    def test_tag_matches_group(self):
        html = '<a href="https://www.facebook.com/Brinkman-Adventures-152895116079/", class="test">hey</a>' \
               '<div class="icon">Facebook</div>'
        soup = bs4.BeautifulSoup(html, 'html.parser')
        self.assertEqual(self.converter.test_if_tag_matches_group(self.rules[0], soup.find('a')), True)
        self.assertEqual(self.converter.test_if_tag_matches_group(self.rules[0], soup.find('div')), False)

    def test_tag_matches_any_rules(self):
        html = '<a href="https://www.facebook.com/Brinkman-Adventures-152895116079/", class="test">hey</a>' \
               '<div class="icon">Facebook</div>'
        soup = bs4.BeautifulSoup(html, 'html.parser')
        self.assertEqual(str(self.converter.test_if_tag_matches_any_rules(self.rules, soup.find('a'))[1][0]),
                         '<a ,="" class="test" href="https://www.facebook.com/Brinkman-Adventures-152895116079/">hey</a>')

    def test_get_matching_tags(self):
        soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.assertEqual(str(self.converter.get_matching_tags(self.rules, soup.find_all())[1][4]),
                         '<a class="xoo-cp-btn-vc xcp-btn" href="https://brinkmanadventures.com/cart">View Cart</a>')
        self.assertEqual(str(self.converter.get_matching_tags(self.rules, soup.find_all())[2][4]),
                         '<link href="https://brinkmanadventures.com/comments/feed" rel="alternate" '
                         'title="Brinkman Adventures » Comments Feed" type="application/rss+xml"/>')


if __name__ == '__main__':
    TestConverter().run()
