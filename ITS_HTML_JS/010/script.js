document.addEventListener("DOMContentLoaded", function () {
    var clicableDiv = document.getElementById("clicableDiv");
    var clicableDiv2 = document.getElementById("clicableDiv2");
    var stranger = document.getElementById("stranger");

    // Способ 2
    clicableDiv.onclick = function () {
        alert("Click from file")
    }

    // Способ 3
    clicableDiv2.addEventListener('click', function () {
        alert("Способ 3")
    });

    // event объект и его свойства 
    function moveDiv(e) {
        //        stranger.style.left = e.pageX + 'px';
        //        stranger.style.top = e.pageY + 'px';
        x.innerHTML = e.pageX;
        y.innerHTML = e.pageY;
    }

    document.body.addEventListener("click", moveDiv);
});

let first_color = "white";
document.body.style.backgroundColor = first_color;

let colors = new Array('red', 'green', 'blue');

let num_color = 0;

function change_color(e) {
    if (e.button == 0) {
        document.body.style.backgroundColor = colors[num_color];
        num_color++;
        if (num_color == colors.length)
            num_color = 0;
    }
    if (e.button == 2) {
        document.body.style.backgroundColor = first_color;
    }
}
btnC.addEventListener('click', change_color);

