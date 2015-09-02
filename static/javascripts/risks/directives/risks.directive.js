(function () {
  'use strict';

  angular.module('daisy.risks.directives')
    .directive('risks', risks);

  function risks() {

    var directive = {
      controller: 'RisksController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        risks: '='
      },
      templateUrl: '/static/templates/risks/risks.html'
    };

    return directive;
  }
})();