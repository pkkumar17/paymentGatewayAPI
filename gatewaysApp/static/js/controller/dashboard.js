
app.controller('dashboarCtrl', function($scope, gateway, $state) {
	
	var details = gateway.openGateway();
    $scope.firstName= details.firstName;
    $scope.lastName= details.lastName;
    $scope.gateways = [
		{
			"name" : "dwolla"
		},
		{
			"name" : "payu"
		},
		{
			"name" : "checkout"
		}
    ];
    
    $scope.selected_gateway = $scope.gateways[0];

    $scope.openGateway = function () {
    	if ($scope.selected_gateway.name = "dwolla") {
    		alert("here it go")
    		$state.go('gateway');
    	}
    }
});