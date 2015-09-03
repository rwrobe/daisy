(function(){
    'use strict';

    angular.module('daisy.risks.controllers')
        .controller('RisksController', RisksController);

    RisksController.$inject = ['$rootScope', '$scope', 'Risks'];

    function RisksController($rootScope, $scope, Risks){
        var vm = this;

        vm.cards = [];
        
        activate();

        function activate(){
            $scope.$watchCollection(function () { return $scope.risks; }, render);
            $scope.$watch(function () { return $(window).width(); }, render);
        }


        function render(current, original) {
            
          if (current !== original) {
            vm.cards = [];

            for (var i = 0; i < 20; ++i) {
              vm.cards.push([]);
            }

            for (var i = 0; i < current.length; ++i) {
              vm.cards[i].push(current[i]);
            }
          }
        }

    }
})();