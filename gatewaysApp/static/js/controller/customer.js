
app.controller('customerCtrl', function($scope, $rootScope, customer, $state) {
	$rootScope.signupbtn = true;
	$scope.customer_data = {};
	$scope.saveCustomer = function (customer_data) {
		customer.postCustomer (customer_data , function (err ,user) {
			if (!err) {
				alert("user saved successcully")
			}
		})
	}
});