var hot = false
var temp = 10
if (temp>80) {
  console.log("Hot Outside!");
} else if (temp <= 80 && temp >= 50) {
  console.log("Warm Outside")
} else if (temp < 50 && temp >= 32) {
  console.log("Cold Outside!")
} else {
  console.log("Freezing Outside!")
}
