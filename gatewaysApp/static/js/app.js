var app = angular.module('myApp', ['ui.router','ngResource']);

app.config(function($stateProvider, $urlRouterProvider) {
    
    
    $stateProvider
        .state('/', {
            url: '/',
            controller:'dashboarCtrl',
            templateUrl: 'static/view/dashboard.html'
        })
        
        .state('gateway', {
            url: '/gateway',
            controller: 'brainteeCtrl',
            templateUrl: 'static/view/braintree.html'
        });
        
    $urlRouterProvider.otherwise('/');

});