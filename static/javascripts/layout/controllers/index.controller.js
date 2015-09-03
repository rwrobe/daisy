(function(){
    'use strict';

    angular.module('daisy.layout.controllers')
        /** @see https://docs.angularjs.org/guide/filter */
        .filter('codeInterpreter', function(){
            return function(code,type){
                var riskList = [
                    {code:101,class:'car',riskFactor:3,message:'Riding in a car'},
                    {code:102,class:'bus',riskFactor:1,message:'Taking the bus'},
                    {code:103,class:'train',riskFactor:1,message:'Taking a train'},
                    {code:104,class:'boat',riskFactor:2,message:'Riding on a boat'},
                    {code:105,class:'plane',riskFactor:0,message:'Taking a plane'},
                    {code:201,class:'work',riskFactor:0,message:'At work'},
                    {code:202,class:'tv',riskFactor:1,message:'Watching TV'},
                    {code:203,class:'reading',riskFactor:1,message:'Reading a book'},
                    {code:301,class:'cardio',riskFactor:2,message:'Performing cardio'},
                    {code:302,class:'strength',riskFactor:3,message:'Feats of strength'},
                    {code:303,class:'zombie',riskFactor:6000000,message:'Hunting Nazi zombies'}
                ];

                for(var key in riskList){
                    if( riskList[key].code === code ){
                        switch(type){
                            case 'class':
                                return riskList[key].class;
                                break;
                            case 'risk':
                                return riskList[key].riskFactor;
                                break;
                            case 'message':
                                return riskList[key].message;
                                break;
                            default:
                                return false;
                                break;
                        }

                    }
                }
            }
        }).filter('rounder', function(){
            return function(num, $scope){
                $scope.Math = window.Math;

                return num.toFixed(2);
            }
        })
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'Authentication', 'Risks', 'Snackbar'];

    function IndexController($scope, Authentication, Risks, Snackbar){
        var vm = this;

        $scope.Math = Math;

        vm.isAuthenticated = Authentication.isAuthenticated();
        vm.risks = [];

        activate();

        function activate(){
            Risks.all().then(onSuccess, onFailure);

            $scope.$on('risk.created', function(e, risk){
                vm.risks.unshift(risk);
            });

            function onSuccess(data, status, headers, config){
                vm.risks = data.data;
            }

            function onFailure(data, status, headers, config){
                $snackbar.error(data.error);
            }
        }
    }

})();