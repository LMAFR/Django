for (var i = 0; i < 5; i++) {
    console.log('hello' [i])
};

var i = 0;
while (i < 5) {
    console.log('hello' [i]);
    i++;
}

function linSpace(startValue, stopValue, Step) {
    var arr = []
    var i = startValue;

    for (startValue; startValue <= stopValue; startValue = startValue + Step) {
        arr.push(startValue)
    }
    return arr
};

var x = linSpace(1, 25, 1);
for (var i = 0; i < 25; i++) {
    if (x[i] % 2 !== 0) {
        console.log(x[i]);
    };
}

var i = 0;
while (i < 25) {
    if (x[i] % 2 !== 0) {
        console.log(x[i]);
    };
    i++;
}