angular.module "fe"
  .factory "restClient", ($http, $q)->

    class Client
      constructor: ()->
        return

      @handlerRequest: (reuqest)->
        defer = $q.defe()
        request.then(
          (resp)->
            defer.resolve(resp.data.data)
          (resp)->
            defer.reject(resp)
        )
        return defer.promise

      @get = (url, params, headers)->
        return @handlerRequest(
          $http(
            method: 'GET'
            url: url
            params: params
            headers: headers
          )
        )

    return Client

