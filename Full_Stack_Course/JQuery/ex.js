// In progress: function encapsulation.

// AN ALERT FOR YOUR NAME (PLAYER 1) AND ANOTHER FOR PLAYER 2

let player1 = prompt("Please enter the name of Player 1", "Harry Potter");
let player2 = prompt("Please enter the name of Player 2", "Draco Malfoy");

if (player1 == null || player1 == "") {
    console.log("User did not write a name for Player1.");
  }

if (player2 == null || player2 == "") {
    console.log("User did not write a name for Player2.");
  }

// When a player clicks on a column, the non-colored circle at the 
// bottom should be colored with the player´s color

let turn = "Player 1";
let done = false;
let k= 0;
// I use the fact that the table is a m*n element to calculate the number of columns as (n_cells/n_rows)
let n_col = $("td").length/$("tr").length;

for(let col = 1; col <= n_col; col++){
    $(`#col${col}`).click(function(){
        for (let tr = $("tr").length; tr > 0; tr--){    
            if (done === false) {
                if ($(`table tr:nth-child(${tr}) td:nth-child(${col})`).css("background-color") === "rgb(255, 255, 255)") {
                    // Player 1
                    if (turn === "Player 1") {
                        // Add color to the circle background
                        $(`table tr:nth-child(${tr}) td:nth-child(${col})`).css("background-color", "rgb(0, 0, 255)");
                        
                        // Check if this player has won in this turn
                        // By row
                        let l = col;
                        while($(`table tr:nth-child(${tr}) td:nth-child(${l})`).css("background-color") === "rgb(0, 0, 255)" & l <= n_col & l > 0){
                            l++;
                            k++;
                            if (k === 4) {
                                alert(`${turn} has won the game!`)
                                // Reset the board
                                $("td").css("background-color", "rgb(255, 255, 255")
                                }
                            }
                        l = col-1;
                        while($(`table tr:nth-child(${tr}) td:nth-child(${l})`).css("background-color") === "rgb(0, 0, 255)" & l <= n_col & l > 0){
                            l--;
                            k++;
                            if (k === 4) {
                                alert(`${turn} has won the game!`)
                                // Reset the board
                                $("td").css("background-color", "rgb(255, 255, 255")
                                }
                            }
                        
                        // Reset the counter
                        k = 0;

                        // By column (simpler, as our pointer is in the current coloured circle and it cannot have coloured circles above itself)
                        let m = tr;
                        while($(`table tr:nth-child(${m}) td:nth-child(${col})`).css("background-color") === "rgb(0, 0, 255)" & m <= $("tr").length & m > 0){
                            m++;
                            k++;
                            if (k === 4) {
                                alert(`${turn} has won the game!`)
                                // Reset the board
                                $("td").css("background-color", "rgb(255, 255, 255")
                                }
                            }
                        // Reset the counter 
                        k = 0;
                    
                        $("h3").text("A: it is your turn, please, pick a column to drop your blue chip.")                       

                        // Stop iterations in the main for loop
                        done = true;
                        // Pass turn
                        turn = "Player 2";
                    }
                    // Player 2
                    else if (turn === "Player 2") {
                        $(`table tr:nth-child(${tr}) td:nth-child(${col})`).css("background-color", "rgb(255, 0, 0)");

                        // Check if this player has won in this turn
                        // By row
                        let l = col;
                        while($(`table tr:nth-child(${tr}) td:nth-child(${l})`).css("background-color") === "rgb(255, 0, 0)" & l <= n_col & l > 0){
                            l++;
                            k++;
                            if (k === 4) {
                                alert(`${turn} has won the game!`)
                                // Reset the board
                                $("td").css("background-color", "rgb(255, 255, 255")
                                }
                            }
                        l = col-1;
                        while($(`table tr:nth-child(${tr}) td:nth-child(${l})`).css("background-color") === "rgb(255, 0, 0)" & l <= n_col & l > 0){
                            l--;
                            k++;
                            if (k === 4) {
                                alert(`${turn} has won the game!`)
                                // Reset the board
                                $("td").css("background-color", "rgb(255, 255, 255")
                                }
                            }
                        
                        // Reset the counter
                        k = 0;

                        // By column (simpler, as our pointer is in the current coloured circle and it cannot have coloured circles above itself)
                        let m = tr;
                        while($(`table tr:nth-child(${m}) td:nth-child(${col})`).css("background-color") === "rgb(255, 0, 0)" & m <= $("tr").length & m > 0){
                            m++;
                            k++;
                            if (k === 4) {
                                alert(`${turn} has won the game!`)
                                // Reset the board
                                $("td").css("background-color", "rgb(255, 255, 255")
                                }
                            }
                        // Reset the counter 
                        k = 0;
                        
                        $("h3").text("B: it is your turn, please, pick a column to drop your red chip.")

                        done = true;
                        turn = "Player 1";
                    }
                }  
            }
            // If a circle has been colored, prepare done for the next iteration and stop the loop.
            else if (done === true){
                done = false;
                break;
            }
        }
    })
}

