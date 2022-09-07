var names = '  ';
names = prompt('What are, in order, your First and Last Name?');
var first_Name = names.split(' ')[0];
var last_Name = names.split(' ')[1];

var age = null;
age = prompt('How old are you? Please, only write the number.');

var height = null;
height = prompt('How tall are you (in centimenters)?');

var pet_Name = null;
pet_Name = prompt('What is the name of your pet?');

alert('Your data has been successfully submitted. Thank you!')

if ((first_Name[0] == last_Name[0]) && ((age > 20) && (age < 30)) && (height >= 170) && (pet_Name.slice(-1) === 'y')) {
    console.log('Hello Spy!');
} else {
    console.log('Who are you?');
}