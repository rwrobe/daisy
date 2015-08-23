(function(){
    'use strict';

    angular
        .module('daisy.authentication',[
            'daisy.authentication.controllers',
            'daisy.authentication.services'
        ]);

    angular
        .module('daisy.authentication.controllers',[]);

    angular
        .module('daisy.authentication.services', ['ngCookies']);
})();