
app.controller('brainteeCtrl', function($scope, gateway, $state) {
	gateway.getToken(function (err, token) {
		if (!err) {
			var clientToken = token.client_token;
			braintree.setup(clientToken, "dropin", {
				container: "payment-form"
			});
		}
	})
	
});