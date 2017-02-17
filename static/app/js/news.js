/**
 * Created by mafz on 16/02/2017.
 */
(function(angular) {
    'use strict';
    angular.module('app', [])
        .controller('newsController', ['newsService', '$scope', function (news, $scope) {
            $scope.bbc = [];
            $scope.cnn = [];

            $scope.onLoad = function () {
                news.getXmlBBC().then(function (response) {
                    var raw = response.data;
                    $(raw).find('item').each(function () { // or "item" or whatever suits your feed
                        var el = $(this);

                        var data = el[0].children;
                        /*
                         0:title
                         1:description
                         2:link
                         3:guid
                         4:pubdate
                         5:media:thumbnail
                         */

                        console.log(data);

                        $scope.bbc.push({
                            title:data[0].text,
                            desc:data[1].innerHTML,
                            link:data[3].innerHTML,
                            img:data[5].attributes[2].nodeValue
                        });

                    });
                });
                news.getRssCNN().then(function (response) {
                    $scope.cnn = response.data;
                });
            }
        }])
        .service('newsService', ['$http', function ($http) {
            this.getXmlBBC = function () {
                return $http.get('/bbc');
            };

            this.getRssCNN = function () {
                return $http.get('/cnn');
            };
        }])
})(window.angular);