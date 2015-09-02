(function(){
    'use strict';

    angular.module('daisy.risks.services')
        .factory('Risks', Risks);

    Risks.$inject = ['$http'];

    function Risks($http){
        var Risks = {
            all: all,
            create: create,
            get: get
        }

        return Risks;

        function all(){
            return $http.get('/api/v1/risks/');
        }

        function create(code, duration){
            return $http.post('/api/v1/risks/', {
               code: code,
               duration: duration
            });
        }

        function get(username){
            return $http.get('/api/v1/accounts/' + username + '/risks/')
        }
    }

})();