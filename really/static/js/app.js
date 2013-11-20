/**
 * Created by mphuie on 11/18/13.
 */
var myApp = angular.module('myApp', ['ui.router'])

myApp.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('root', {url: '/root', templateUrl:'/static/partials/root.html'})
        .state('home', { url: '/home', templateUrl: '/static/partials/home.html'})
        .state('list', { url: '/list', templateUrl: '/static/partials/list.html'})
        .state('list.item', {
            url: '/:item',
            templateUrl: 'static/partials/list.item.html',
            controller: function($scope, $stateParams) {
                $scope.item = $stateParams.item;
            }
        })

    $urlRouterProvider.otherwise('/root');
})

myApp.controller('MyController', function($scope, $http) {

    $scope.shoppingList = [
        {name: 'Milk'},
        {name: 'Eggs'},
        {name: 'Bread'},
        {name: 'Cheese'},
        {name: 'Ham'}
    ];




});