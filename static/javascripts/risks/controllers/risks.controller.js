(function(){
    'use strict';

    angular.module('daisy.risks.controllers')
        .controller('RisksController', RisksController);

    RisksController.$inject = ['$rootScope', '$scope', 'Risks'];

    function RisksController($rootScope, $scope, Risks){
        var vm = this;

        vm.columns = [];

        vm.riskList = [{
                code: 101,
                class: 'car'
            }, {
                code: 102,
                class: 'bus'
            }, {
                code: 103,
                class: 'train'
            }, {
                code: 104,
                class: 'boat'
            }, {
                code: 105,
                class: 'plane'
            }, {
                code: 201,
                class: 'work'
            }, {
                code: 202,
                class: 'tv'
            }, {
                code: 203,
                class: 'reading'
            }, {
                code: 301,
                class: 'cardio'
            }, {
                code: 302,
                class: 'strength'
            }, {
                code: 303,
                class: 'zombie'
            }];

        activate();
        codeConverter();

        function activate(){
            $scope.$watchCollection(function () { return $scope.risks; }, render);
            $scope.$watch(function () { return $(window).width(); }, render);
        }

        /**
         * Returns the associated class of the object
         * @param code
         * @returns {*}
         */
        function getClass(code){
            for(var key in riskList){
                if( riskList[key].code === code ){
                    return riskList[key].class;
                }
            }
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