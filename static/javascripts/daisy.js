angular
  .module('daisy', [
        'daisy.config',
        'daisy.routes',
        'daisy.authentication',
        'daisy.layout',
        'daisy.risks',
        'daisy.utils',
    ]);

angular
    .module('daisy.config',[]);

angular
    .module('daisy.routes', ['ngRoute']);

angular
    .module('daisy')
    .run(run);

run.$inject = ['$http'];

function run($http){
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}