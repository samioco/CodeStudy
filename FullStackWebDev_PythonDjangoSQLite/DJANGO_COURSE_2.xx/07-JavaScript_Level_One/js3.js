var hot = false
var temp = 10
console.log("Temp: "+temp)
if (temp>80) {
  console.log("Hot Outside!");
} else if (temp <= 80 && temp >= 50) {
  console.log("Warm Outside")
} else if (temp < 50 && temp >= 32) {
  console.log("Cold Outside!")
} else {
  console.log("Freezing Outside!")
}


var ham = 10
var cheese = 10
console.log("")
console.log("Ham: "+ham+", Cheese: "+cheese)
if (ham>=10 && cheese>=10) {
  report="Lots of ham and cheese sold!"
} else if (ham===0 && cheese===0) {
  report="Nothing sold!"
} else {
  report="Some sold!"
}

console.log(report)
