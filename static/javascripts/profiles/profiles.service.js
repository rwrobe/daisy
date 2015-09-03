(function () {
  'use strict';

  angular
    .module('daisy.profiles.services')
    .factory('Profile', Profile);

  Profile.$inject = ['$http'];

  function Profile($http) {

    var Profile = {
      destroy: destroy,
      get: get,
      update: update
    };

    return Profile;

    function destroy(profile) {
      return $http.delete('/api/v1/users/' + profile.id + '/');
    }
      
    function get(username) {
      return $http.get('/api/v1/users/' + username + '/');
    }

      function update(profile) {
      return $http.put('/api/v1/users/' + profile.username + '/', profile);
    }
  }
})();