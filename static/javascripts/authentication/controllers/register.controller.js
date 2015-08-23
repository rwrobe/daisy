(function(){
    'use strict';

    angular.module('daisy.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    function RegisterController($location, $scope, Authentication){
        var vm = this;

        vm.register = register;

        /** Kick them to the homepage if already registered and logged in */
        activate();

        function activate(){
           if( Authentication.isAuthenticated() )
            $location.url('/');
        }

        function register(){
            Authentication.register(vm.email, vm.username, vm.password);
        }
    }
})();