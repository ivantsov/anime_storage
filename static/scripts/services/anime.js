(function () {
    'use strict';

    angular
        .module('main')
        .factory('Anime', Anime);

    function Anime($resource) {
        return $resource('api/anime/:id', {id: '@id'}, {
            update: {
                method: 'PUT'
            }
        });
    }
})();