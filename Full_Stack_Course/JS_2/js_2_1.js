//  Function 1
// function sleepIn(weekday, vacation) {
//     if (!weekday || vacation) {
//         return true;
//     }
//     return false;
// }

// console.log(sleepIn(false, false))
// console.log(sleepIn(true, false))
// console.log(sleepIn(false, true))

// Function 2
// function monkeyTrouble(aSmile, bSmile) {
//     if ((aSmile && bSmile) || (!aSmile && !bSmile)) {
//         return true;
//     }
//     return false;
// }

// console.log(monkeyTrouble(true, true))
// console.log(monkeyTrouble(false, false))
// console.log(monkeyTrouble(true, false))

// Function 3
// function stringTimes(string_var, non_neg_int) {
//     if (non_neg_int >= 0) {
//         console.log(string_var.repeat(non_neg_int))
//     } else {
//         console.log('The input was not a non negative integer')
//     }
// }

// stringTimes('Hi', 2)
// stringTimes('Hi', 3)
// stringTimes('Hi', 1)

// Function 4
// function luckySum(a, b, c) {
//     var lista = [a, b, c];
//     var suma = 0;
//     for (var i = 0; i < lista.length; i++) {
//         if (lista[i] != 13) {
//             suma += lista[i]
//         } else {
//             break
//         }
//     }
//     return suma
// }

// console.log(luckySum(1, 2, 3))
// console.log(luckySum(1, 2, 13))
// console.log(luckySum(1, 13, 3))

// Function 5
// function caught_speeding(speed, birthday) {
//     var ticket = null;
//     if (!birthday) {
//         if (speed <= 60) {
//             ticket = 0;
//         } else if ((speed >= 60) && (speed <= 80)) {
//             ticket = 1;
//         } else if (speed >= 81) {
//             ticket = 2;
//         }
//     } else if (birthday) {
//         if (speed <= 60 * 5) {
//             ticket = 0;
//         } else if ((speed >= 60 * 5) && (speed <= 80 * 5)) {
//             ticket = 1;
//         } else if (speed >= 81 * 5) {
//             ticket = 2;
//         }
//     }
//     return ticket
// }

// console.log(caught_speeding(60, false))
// console.log(caught_speeding(65, false))
// console.log(caught_speeding(65, true))

// Bonus Function
// function makeBricks(small_bricks_number, big_bricks_number, goal) {
//     var cociente = Math.floor(goal / 5)
//     var resto = goal % 5
//     if ((resto === 0) && (cociente <= big_bricks_number)) {
//         return true;
//     } else if ((resto !== 0) && (cociente <= big_bricks_number) && (resto <= small_bricks_number)) {
//         return true;
//     }
//     return false;
// }

// console.log(makeBricks(3, 1, 8))
// console.log(makeBricks(3, 1, 9))
// console.log(makeBricks(3, 2, 10))