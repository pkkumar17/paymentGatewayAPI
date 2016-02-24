
app.controller('dashboarCtrl', function($scope, $rootScope, gateway, $state) {
	var details = gateway.openGateway();
    $rootScope.signupbtn = false;
    $scope.firstName= details.firstName;
    $scope.lastName= details.lastName;
    gateway.getPaymentGatewayList(function(err, list){
    	if (!err) {
    		$scope.gateways = list;
    		$scope.selected_gateway = $scope.gateways[0];
    	}
    })

    $scope.openGateway = function () {
    	if ($scope.selected_gateway.name = "dwolla") {
    		$state.go('gateway');
    	}
    }

    $rootScope.customerSingup = function () {
        $state.go('customer');
    }
});