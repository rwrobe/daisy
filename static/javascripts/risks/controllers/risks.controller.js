(function(){
    'use strict';

    angular.module('daisy.risks.controllers')
        .controller('RisksController', RisksController);

    RisksController.$inject = ['$rootScope', '$scope', 'Risks'];

    function RisksController($rootScope, $scope, Risks){
        var vm = this;

        vm.columns = [];
        
        activate();

        function activate(){
            $scope.$watchCollection(function () { return $scope.risks; }, render);
            $scope.$watch(function () { return $(window).width(); }, render);
        }

        function approximateShortestColumn() {
            var scores = vm.columns.map(columnMapFn);

            return scores.indexOf(Math.min.apply(this, scores));


            function columnMapFn(column) {
                var lengths = column.map(function (element) {
                  return element.length;
                });

                return lengths.reduce(sum, 0) * column.length;
            }


             function sum(m, n) {
                return m + n;
             }
        }

        function render(current, original) {
          if (current !== original) {
            vm.columns = [];

            for (var i = 0; i < 20; ++i) {
              vm.columns.push([]);
            }

            for (var i = 0; i < current.length; ++i) {
              var column = approximateShortestColumn();

              vm.columns[i].push(current[i]);
            }
          }
        }

        function destroy() {
            Risk.destroy(vm.risk.id).then(onDelSuccess, onDelFailure);

            function onDelSuccess(data, status, headers, config) {
                Snackbar.show('Good to be safe.');
            }

            function onDelFailure(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }
    }
})();