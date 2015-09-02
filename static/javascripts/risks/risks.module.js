(function(){
    'use strict';

    angular.module('daisy.risks', [
        'daisy.risks.controllers',
        'daisy.risks.directives',
        'daisy.risks.services'
    ]);

    angular.module('daisy.risks.controllers',[]);

    angular.module('daisy.risks.directives', ['ngDialog']);

    angular.module('daisy.risks.services',[]);

})();