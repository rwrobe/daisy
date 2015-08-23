(function () {
  'use strict';

  angular.module('daisy.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http'];

  function Authentication($cookies, $http) {

    var Authentication = {
      register: register
    };

    return Authentication;

    function register(email, username, password) {
      return $http.post('/api/v1/accounts/', {
        email: email,
        username: username,
        password: password
      });
    }
  }
})();