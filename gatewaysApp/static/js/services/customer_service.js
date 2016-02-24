
app.factory('customer', function($resource) {
	return {
		postCustomer : function (data, callback) {
			//hit api
			var customer = $resource('/registration/', {},
									{
										'save':
											{
												'method':'POST'
											}
									}, {});
			console.log(JSON.stringify(data));
			customer.save(data,function (list) {
				callback(null, list)
			})
		}
	}
});