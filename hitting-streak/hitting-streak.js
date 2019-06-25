// Usage: `node THIS_FILE.js`

// returns true if the player 'hit' the ball
const swing = avg => Math.random() <= avg;

// A game has a base hit if the player hits any of the 12 balls thrown at him
const game = avg => {
    for (var i=0; i<4; i++){
        if (swing(avg)){
            return true
        }
    }
    return false;
}

// Returns the number of connsecutive truthy things in a row.
const numConnsec = input => {
    var largestSeen =0;
    var currentSequence = 0;

    for (var i=0; i < input.length ; i++) {
        if (input[i]){
            currentSequence ++
        } else {
            largestSeen = currentSequence > largestSeen ? currentSequence : largestSeen;
            currentSequence =0;
        }
    }

    largestSeen = currentSequence > largestSeen ? currentSequence : largestSeen;
    return largestSeen;
}

// "unit tests"
const tests = [
    [[], 0],
    [[0], 0],
    [[1], 1],
    [[1, true, "a", "", 0], 3],
    [[1,0,0 ], 1],
    [[1,1,0 ], 2],
    [[0,1,1 ], 2],
    [[0,0,1 ], 1],
    [[0,0,0 ], 0],
    [[1,1,1 ], 3],
]

for(var i=0; i<tests.length; i++){
    var list = tests[i][0]
    var exp_result = tests[i][1]
    var result = numConnsec(list)
    if (result !== exp_result){
        console.log(`${list} returned ${result} and not ${exp_result}`)
        throw new Error("woops");
    }
}

let numTests = 10000;
const runTests = (avg, numGames) => {

    var totalStreakBreaks=0;

    for (var i=0; i<numTests; i++){
        var games = [];

        // run a player's career
        for (j=0; j<numGames; j++){
            games.push(game(avg))
        }

        if (numConnsec(games) > 58){
            totalStreakBreaks++
        }

    }
    return 100*totalStreakBreaks/numTests;
}

let GAMES_PER_SEASON=160
players_games = [
        [ .200, 20*GAMES_PER_SEASON ],
        [ .250, 20*GAMES_PER_SEASON ],
        [ .300, 20*GAMES_PER_SEASON ],
        [ .350, 20*GAMES_PER_SEASON ],
        [ .400, 20*GAMES_PER_SEASON ],
        [ .500, 10*GAMES_PER_SEASON ],
    ]

for (var i=0; i <players_games.length; i++){

    var avg = players_games[i][0];
    var games = players_games[i][1];

    var percentage = runTests(avg, games)
    console.log(`${avg} will beat the streak with ${games} games ${percentage} percent of the time`)
}
