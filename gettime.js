// Converts given time to just minutes ie "1 hour 20 mins" == "80"
function PARSETIME(output) {
    var minutes = 0;

    // Google's Script enviroment lacks the capabilities to use "str.includes('')"
    if (output.indexOf('hour') >= 0) {
        var hour = output.split(" hour")[0];
        hour = parseInt(hour, 10);

        minutes += (hour * 60);

        outmin = output.split(" hour")[1];
        outmin = parseInt(outmin, 10);
        minutes += outmin;
    } else {
        minutes += parseInt(output, 10);
    }

    return minutes;
}


// by e__n on StackOverflow: https://stackoverflow.com/a/50921934
// I added the location2 workaround

//locations can be addresses or coordinates
//allowed modes are DRIVING, WALKING, BICYCLING, TRANSIT
function GETTIME(location1, location2, mode) {
    if (location2 == "WORK") {
        location2 = " ";
    } else if (location2 == "SOCIAL") {
        location2 = " ";
    }

    var directions = Maps.newDirectionFinder()
        .setOrigin(location1)
        .setDestination(location2)
        .setMode(Maps.DirectionFinder.Mode[mode])
        .getDirections();
    var output = directions.routes[0].legs[0].duration.text;
    
    return PARSETIME(output);
}