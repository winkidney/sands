angular.module "fe"
  .factory "auth", ($q, RestClient)->
    client = new RestClient()
    loginInfo =
      logined: false
      username: null

    login = (username, password)->
      defer = $q.defer()
      client.post("/login", {username: username, password: password})
      .then(
        (data)->
          loginInfo.logined = true
          login.username = data.username
          defer.resolve(defer)
        (resp)->
          defer.reject(defer)
      )