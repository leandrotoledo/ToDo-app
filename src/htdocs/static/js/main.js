var app = angular.module('noteApp', [])

app.controller('NoteAddCtrl', function($scope, $http) {
    $scope.submit = function() {
        $http.post('http://127.0.0.1:5000/notes', {'annotation': $scope.annotation}).
            then(function(response) {
                console.log('Success!')
            }, function(response) {
                console.log(response)
            });
    };
});
