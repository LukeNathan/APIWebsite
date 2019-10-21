var myData = "";
var staticUrl = 'https://restcountries.eu/rest/v2/all'; 

$.getJSON(staticUrl, function(data) {
        console.log(data)
    });