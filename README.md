# Welcome to My First Scraper
***

# Introduction

<img width="495" alt="meme_scraping" src="https://user-images.githubusercontent.com/95611906/200126969-42bdcb8b-b0ab-4a29-9fb2-d21a3bc5d2f2.png">

<p>HTML has been built to be "displayed". It's working very well... but when you want to build a script to collect actionable data, you are left with this:</p>
```bash
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head>
<meta charset="UTF-8"><meta content="origin" name="referrer"><meta content="Search the 
world's information,including webpages, images, videos and more. Google has many special
features to help you find exactly what you're looking for." name="description"><meta content="noodp"
name="robots">meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" 
itemprop="image"><meta content="origin" name="referrer"><title>Google</title><script 
nonce="RV78oTZM3BoorRaUbY2QZQ==">(function(){window.google={kEI:'Axs7X5WnBMut0PEPi5OcwAI',kEXPI:'31'
,u:'8804ad99',kBL:'vHaf'};google.sn='webhp';google.kHL='en';})();(function(){google.lc=[];
google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)
a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute
||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};
google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl
(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function()
{delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.
logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.
getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-
window.performance&&window.performance.navigation&&window.performance.navigation.type};function
k(a,b){return!a||!b&&l(a)?0:a.getBoundingClientRect?m(a,b,function(c){return c.getBoundingClientRect()})
:1}function l(a){if("none"==a.style.display)return!0;if(document.defaultView&&document
.defaultView.getComputedStyle){var b=a.getAttribute("data-deferred");b&&a.setAttribute
("data-deferred",0);var c=document.defaultView.getComputedStyle(a);c=!!c&&("hidden"==c.visibility|
|"0px"==c.height&&"0px"==c.width);b&&a.setAttribute("data-deferred",b);return c}return!1}
function m(a,b,c){var d=c(a);a=d.left+window.pageXOffset;c=d.top+window.pageYOffset;var
e=d.width;d=d.height;var f=0;if(!b&&0>=d&&0>=e)return f;0>c+d?f=2:c>=(window.innerHeight||document.documentElement.clientHeight)&&(f=4);if(0>a+e||a>=(window.innerWi....
0==c.returnValue)c.returnValue=!0}c=[];for(d=b.a;d;d=d.parentNode)c.push(d);a=a.type;for(d=
c.length-1;0<=d;d--){b.a=c[d];var f=Aa(c[d],a,!0,b);e=e&&f}for(d=0;d<c.length;d++)b.a=c[d],
f=Aa(c[d],a,!1,b),e=e&&f}return e}return za(a,new T(b,this))},Y=function(a){a=a[W];return a
instanceof V?a:null},Z="__closure_events_fn_"+(1E9*Math.random()>>>0),ua=function(a){if
("function"==aa(a))return a;a[Z]||(a[Z]=function(b){return a.handleEvent(b)});return a[Z]};
ta(document,"DOMContentLoaded",function(){document.f&&(document.f.q.getAttribute("data-saf")
||document.f.q.focus());document.gbqf&&document.gbqf.q.focus();document.images&&((new Image)
.src=s)});})();</script></div><textarea class="csi" name="csi" style="display:none"></textarea>
<script nonce="RV78oTZM3BoorRaUbY2QZQ==">(function(){function(){var c=google.time();if
(google.timers&&google.timers.load.t){for(var a=document.getElementsByTagName("img"),d=0,b=void 0
;b=a[d++];)google.c.setup(b);google.c.e("load","imn",String(a.length));google.c.ubr(!0,c);google.c
.glu&&google.c.glu();google.rll(window,!1,function(){google.tick("load","ol");google.c.u("pr")}
)}})();}).call(this);google.drty&&google.drty();</script></body></html>
```

<a href="https://github.com/trending">Github trending's page</a>

<a href="https://abdullaabdukulov-my-first-scraper-app-1p3avr.streamlit.app/">on the website</a>

<img width="2048" alt="image" src="https://user-images.githubusercontent.com/95611906/200126357-99ec6ad4-e6df-48e1-9a28-bd84256709d8.png">
