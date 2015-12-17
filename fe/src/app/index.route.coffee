angular.module 'fe'
  .config ($stateProvider, $urlRouterProvider) ->
    'ngInject'
    $stateProvider
      .state 'home',
        url: '/home'
        templateUrl: 'app/main/main.html'
        controller: 'MainController'
        controllerAs: 'main'
      .state 'new',
        url: '/new'
        templateUrl: 'app/main/main.html'
        controller: 'MainController'
        controllerAs: 'new'
      .state 'about',
        url: '/about'
        templateUrl: 'app/main/main.html'
        controller: 'MainController'
        controllerAs: 'about'

    $urlRouterProvider.otherwise '/home'
