var restart_button = document.querySelector("#restart_button")
var squares = document.querySelectorAll("#square")

function clearBoard(){
    for (var i = 0; i < squares.length; i++) {
      squares[i] = ""
    }
}
restart_button.addEventListener('click',clearBoard)


// Create a function that will check the square marker
function changeMarker(){
    if(this.textContent === ''){
      this.textContent = 'X';
      // console.log(marker)
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}
