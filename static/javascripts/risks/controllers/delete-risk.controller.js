(function(){
    'use strict';

    angular.module('daisy.risks.controllers')
        .controller('DeleteRiskController', DeleteRiskController);

    DeleteRiskController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Risks'];

    function DeleteRiskController($rootScope, $scope, Authentication, Snackbar, Risks){

        var vm = this;

        vm.destroy = destroy;

        function destroy(){

            $rootScope.$broadcast('risk.destroyed', {
                user: {
                    username: Authentication.getAuthenticatedAccount().username
                },
                id: id
            });

            $scope.closeThisDialog();

            Risks.destroy(vm.id).then(delOnSuccess, delOnFailure);

            function delOnSuccess(data, status, headers, config){

                var messageArray = [
                    'Thank God, don\'t ever do that again',
                    'Smart move. For once.'
                ];

                Snackbar.show(messageArray[Math.floor(Math.random() * messageArray.length)]);
            }

            function delOnFailure(data, status, headers, config){
                $rootScope.$broadcast('risk.destroyed.error');
                Snackbar.error(data.error);
            }
        }
    }
})();