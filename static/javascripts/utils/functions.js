var Daisy = (function($){

    var init = function(){

        counterAdd();

        $('body').on('DOMNodeInserted', 'risk', function(){
            counterAdd();
        });
    };

    var counterAdd = function(){
            var num = $('span.code').html();
            console.log(num);
            num = num.substr(0,4);
    };

    return {
        init: init
    }

})(jQuery);

jQuery(document).ready( function() {
	//Daisy.init();
});