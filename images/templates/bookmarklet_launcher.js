'use strict'
(function(){
    // The preceding script discovers whether the bookmarklet has already been loaded 
    //by checking whether the myBookmarklet variable is defined.
    if (window.myBookmarklet !== undefined){
    myBookmarklet();
    }
    else {
    document.body.appendChild(document.createElement('script')).src='https://127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
   })();
   