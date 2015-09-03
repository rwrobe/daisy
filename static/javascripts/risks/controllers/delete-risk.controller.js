(function(){
    'use strict';

    angular.module('daisy.risks.controllers')
        .controller('DeleteRiskController', DeleteRiskController);

    DeleteRiskController.$inject['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Risks'];

    function DeleteRiskController($rootScope, $scope, Authentication, Snackbar, Risks){

        var vm = this;

        vm.deleteRisk = deleteRisk;

        function deleteRisk(){

            $rootScope.$broadcast('risk.deleted', {
                user: {
                    username: Authentication.getAuthenticatedAccount().username
                },
                id: id
            });

            $scope.closeThisDialog();

            Risks.create(vm.id).then(createOnSuccess, createOnFailure);

            function createOnSuccess(data, status, headers, config){

                Snackbar.show('Activity deleted');
            }

            function createOnFailure(data, status, headers, config){
                $rootScope.$broadcast('risk.deleted.error');
                Snackbar.error(data.error);
            }
        }
    }

})();