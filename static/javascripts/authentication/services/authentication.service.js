(function () {
  'use strict';

  angular.module('daisy.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http', 'Snackbar'];

  function Authentication($cookies, $http, Snackbar) {

    /** Expose the class method */
    var Authentication = {
      login: login,
      logout: logout,
      register: register,
      getAuthenticatedAccount: getAuthenticatedAccount,
      isAuthenticated: isAuthenticated,
      setAuthenticatedAccount: setAuthenticatedAccount,
      unauthenticate: unauthenticate
    };

    return Authentication;

    /** Send the two POST vars to the API endpoint to log the user in */
    function login(email, password){
        return $http.post('/api/v1/auth/login/',{
           email: email,
           password: password
        }).then(onSuccess, onFailure);

        /** Redirect the user on success or failure */
        function onSuccess(data, status, headers, config){
            Authentication.setAuthenticatedAccount(data.data);

            window.location = '/';
        }

        function onFailure(data, status, headers, config){
            //window.location = '/login'
            Snackbar.show('Wrong user/pass combo. I suspect you need more practice operating your keyboard.');
        }
    }

    function logout(){
        return $http.post('/api/v1/auth/logout/')
            .then(logoutSuccess, logoutFailure);

        function logoutSuccess(data, status, headers, config){
            Authentication.unauthenticate();

            window.location ='/';
        }

        function logoutFailure(data, status, headers, config){
            console.log('what does this even mean?');
        }
    }

    /** Three pieces of info to register */
    function register(email, username, password) {
      return $http.post('/api/v1/accounts/', {
        email: email,
        username: username,
        password: password
      }).then(registerSuccess, registerFailure);
    }

    function registerSuccess(data, status, headers, config){
        Authentication.login(email, password);
    }

    function registerFailure(data, status, headers, config){
        window.location = '/register';

        /** @todo Add flash notification on failure */
    }

    /** Return the parsed authenticatedAccount */
    function getAuthenticatedAccount(){
        if( ! $cookies.authenticatedAccount )
            return false;

        return JSON.parse($cookies.authenticatedAccount);
    }

    /** Return the bool for the cookie */
    function isAuthenticated(){
        return !!$cookies.authenticatedAccount;
    }

    /** Set cookie to a string version of the account obj */
    function setAuthenticatedAccount(account){
        $cookies.authenticatedAccount = JSON.stringify(account);
    }

    /** For logging out, remove the cookie */
    function unauthenticate(){
        delete $cookies.authenticatedAccount;
    }
  }
})();