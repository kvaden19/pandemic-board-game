// SETUP
// Player setup
    // How many players?
        // Choose your color (out of ...?)
        // let startingHand = 4, 3, or 2
    // let difficulty = 4, 5, or 6

// Game setup
    // Research station in Atlanta
    // All players in Atlanta
    // let outbreaks = 0;
    // Set up 4 disease objects
        // Colors red, blue, yellow, black
        // Cured and Eradicated set to false
        // Cubes = 96
    // let infectionRate = 2;
    // let masterCities = an array of the 48 city names (ranked by pop)
        // let infectionDeck = a copy of masterCities
        // let playerCards = copy of masterCities
        // randomize both
    // let infectionDiscard = [];
    // let playerDiscard = [];
    // for (3, 2, 1):
        // pop off 3 items from infectionCards; add to infectionDiscard
        // add # disease cubes to each
    // depending on # of players, pop startingHand number of strings off playerCards and onto player.hand
    // shuffle in Epidemic cards
        // divide playerCards into difficulty # of subarrays
        // push one 'epidemic' string onto each array and randomize
        // combine subarrays
    
// GAMEPLAY
    // Choose player order based on highest ranking city card
    // WHILE (outbreaks < 8 AND all disease.cubes > 0 AND playerCards not empty AND ! all disease.cured)
        // Set active player
        // For 4 actions:
            // Show player menu of options:
                // Drive
                // Direct Flight
                // Charter Flight
                // Shuttle Flight
                // Build Station
                // Treat
                // Share
                // Cure
        // Pop 2 items off playerCards into player.hand
            // if epidemic then handle:
                // get item from "opposite" side of array
                // infectionRate ++
                // randomize infectionDiscard, push onto infectionDeck, empty infectionDiscard
        // Pop infectionRate items off infectionDeck into infectionDiscard
            // city.cubes ++
    // Handle win or loss
// Stats tracking?
// Ask to play again
    