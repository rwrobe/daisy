(function(){
    'use strict';

    angular.module('daisy.risks.controllers')
        .controller('NewRiskController', NewRiskController);

    NewRiskController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Risks'];

    function NewRiskController($rootScope, $scope, Authentication, Snackbar, Risks){

        var vm = this;

        vm.submit = submit;

        function submit(){

            $rootScope.$broadcast('risk.created', {
                user: {
                    username: Authentication.getAuthenticatedAccount().username
                },
                code: vm.code,
                duration: vm.duration,
            });

            $scope.closeThisDialog();

            Risks.create(vm.code, vm.duration, vm.rating).then(createOnSuccess, createOnFailure);

            function createOnSuccess(data, status, headers, config){

                var messageArray = [
                    'You <em>do</em> lead a risky life',
                    'Whoa, slow down there kid or you\'ll hurt yourself',
                    'Don\'t take your guns to town son',
                    'Darwin Awards here you come!',
                    'I\'ll take Embarrassing Epitaphs for <strong>200</strong> Alex',
                    'I wouldn\'t do that if I were you',
                    'At your age?',
                    'My grandpa died doing that, and you\'re not half the man he was.'
                ];

                Snackbar.show(messageArray[Math.floor(Math.random() * messageArray.length)]);
            }

            function createOnFailure(data, status, headers, config){
                $rootScope.$broadcast('risk.created.error');
                Snackbar.error(data.error);
            }
        }
    }
})();