(function(){
    'use strict';

    angular.module('daisy.risks.services')
        .factory('Risks', Risks);

    Risks.$inject = ['$http'];

    function Risks($http){
        var Risks = {
            all: all,
            create: create,
            destroy: destroy,
            get: get
        }

        return Risks;

        function all(){
            return $http.get('/api/v1/risks/');
        }

        function create(code, duration, rating){
            return $http.post('/api/v1/risks/', {
                code: code,
                duration: duration,
                rating: rating
            });
        }

        function destroy(id){
            return $http.delete('/api/v1/risks/' + id + '/');
        }

        function get(username){
            return $http.get('/api/v1/users/' + username + '/risks/')
        }
    }

})();