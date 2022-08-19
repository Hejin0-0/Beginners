const images = ["0.jpg", "1.jpg", "2.jpg"];

const chosenImage = images[Math.floor(Math.random() * images.length)];

const bgImage = document.createElement("img");

bgImage.src = `img/${chosenImage}`;
// == html -> div -> <img src='img/0.jpg'>

document.body.appendChild(bgImage);
// html.body에 (bgImage)를 추가
