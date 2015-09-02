(function () {
  'use strict';

  angular.module('daisy.risks.directives')
    .directive('risk', risk);

  function risk() {

    var directive = {
      restrict: 'E',
      scope: {
        risk: '='
      },
      templateUrl: '/static/templates/risks/risk.html'
    };

    return directive;
  }
})();