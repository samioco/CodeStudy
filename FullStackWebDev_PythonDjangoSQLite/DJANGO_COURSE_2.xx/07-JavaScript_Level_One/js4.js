/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////


//print (console.log()) out the word "hello" 5 times.
//For Loop
console.log("For Loop: 5xhello");
for (i = 0; i < 5; i++) {
  console.log("hello");
}
console.log("");

// While Loop
console.log("While Loop: 5xhello");
var i = 0
while (i<5) {
  console.log("hello");
  i++
}
console.log("");

/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
console.log("While Loop: Odd #s 1-25");
var i = 1
while (i<=25) {
  if (i%2===1) {console.log("Odd: "+i);}
  i++
}
console.log("");

// METHOD TWO
// For Loop
console.log("For Loop: Odd #s 1-25");
for (i =1; i<=25; i++) {
  if (i%2===1) {console.log("Odd: "+i);}
}
console.log("");
