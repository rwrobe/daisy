(function () {
  'use strict';

  angular.module('daisy.layout.controllers')
    .controller('LinkController', LinkController);

  LinkController.$inject = ['$scope', 'Authentication'];

  function LinkController($scope, Authentication) {
    var vm = this;

    vm.logout = logout;

    function logout() {
      Authentication.logout();
    }
  }
})();