let colors = ['blue', 'brown', 'turquoise', 'purple', 'lightgreen'];

let backgroundbutton = document.getElementById('backgroundbutton');

backgroundbutton.addEventListener('click', function(){
    var randomcolor = colors[Math.floor(Math.random() * colors.length)]
    let content = document.getElementById('content');
    content.style.background = randomcolor;
})

let Small = document.getElementById('Small');
Small.addEventListener('click', function(){
    let content = document.getElementById('box5');
    content.style.fontSize = '2em';
})
let Medium = document.getElementById('Medium');
Medium.addEventListener('click', function(){
    let content = document.getElementById('box5');
    content.style.fontSize = '3em';
})
let Large = document.getElementById('Large');
Large.addEventListener('click', function(){
    let content = document.getElementById('box5');
    content.style.fontSize = '5em';
})