
app.factory('gateway', function($resource) {
	return {
		openGateway : function() {
		    var details = {"firstName" : "John", "lastName" : "Doe"};
		    return details;
		},

		getToken : function() {
			// hit api
			// var url = $resource('/api/entries/:id', {}, {});
			// url.get({},function (token) {
			// 	console.log(JSON.stringify(token));
			// })
		},

		getPaymentGatewayList : function () {
			//hit api
			// var url = $resource('/api/entries/:id', {}, {});
			// url.query({},function (list) {
			// 	console.log(JSON.stringify(list));
			// })
		}
	}
});