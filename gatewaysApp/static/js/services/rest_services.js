
app.factory('gateway', function($resource) {
	return {
		openGateway : function() {
		    var details = {"firstName" : "John", "lastName" : "Doe"};
		    return details;
		},

		getToken : function(callback) {
			var url = $resource('/getToken/', {}, {});
			url.get({},function (token) {
				callback (null, token)
			})
		},

		getPaymentGatewayList : function (callback) {
			//hit api
			var url = $resource('/gatewaysList/?format=json', {}, {});
			url.query({},function (list) {
				callback(null, list)
			})
		}
	}
});