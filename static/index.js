var i = 0;
var txt = 'It’s the year 2079, the group MZBA has vandalised the world’s largest online encyclopedia. Now we need you to';
var speed = 50;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("introMessage").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
  else {
    document.getElementById("introHeader").style.display = "block";
    setTimeout(function () {
      document.getElementById("introHeader").className += " faded";
    }, 50)
    setTimeout(function () {
      document.getElementById("introButtons").style.display = "block";
    }, 600)
    setTimeout(function () {
      document.getElementById("introButtons").className += " faded";
    }, 680)
  }
}

typeWriter()