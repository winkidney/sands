angular.module 'fe'
  .directive 'acmeNavbar', ->

    NavbarController = (moment, $state, $log) ->
      'ngInject'
      vm = this
      vm.isActive = (stateName)->
        $log.debug "Current state is:", $state.current
        return $state.current.name is stateName
      return

    directive =
      restrict: 'E'
      templateUrl: 'app/components/ui/navbar/navbar.html'
      scope: creationDate: '='
      controller: NavbarController
      controllerAs: 'navbar'
      bindToController: true
