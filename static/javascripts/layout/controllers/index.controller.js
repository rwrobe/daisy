(function(){
    'use strict';

    angular.module('daisy.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'Authentication', 'Risks', 'Snackbar'];

    function IndexController($scope, Authentication, Risks, Snackbar){
        var vm = this;

        vm.isAuthenticated = Authentication.isAuthenticated();
        vm.risks = [];

        activate();

        function activate(){
            Risks.all().then(onSuccess, onFailure);

            $scope.$on('risk.created', function(e, risk){
                vm.risks.unshift(risk);
            });

            function onSuccess(data, status, headers, config){
                vm.risks = data.data;
            }

            function onFailure(data, status, headers, config){
                $snackbar.error(data.error);
            }
        }
    }

})();