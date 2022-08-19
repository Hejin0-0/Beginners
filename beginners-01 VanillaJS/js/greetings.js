/*
const loginForm = document.getElementById('login-form');
const loginButton = loginForm.querySelector('button');
const loginInput = loginForm.querySelector('input'); 
//document(index.html)에서 찾는 대신 loginFrom에서 검색
*/

// 위와 같은 과정을 거치지 않고 id를 통해 바로 검색
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
// string만 포함된 변수는 대문자로 표기하고 저장하고 싶을 때 사용
const USERNAME_KEY = "username";

function onLoginSubmit(event) {
  event.preventDefault();
  // preventDefault() => 어떤 event의 기본 행동이든지 발생되지 않도록 막는 함수
  // 기본 행동 = 어떤 함수에 대해 브라우저가 기본적으로 수행하는 동작
  // ex)누군가 form을 submit하면 기본적으로 페이지를 새로고침 하도록 되어 있는 것
  loginForm.classList.add(HIDDEN_CLASSNAME);
  // submit동작이 실행되었을 때 로그인 form을 안보이게 하기 위함
  // HTML의 어느 한 부분을 잡고 거기에 class 를 추가하거나 빼고 싶을 때는
  // classList.add.('classname') or classList.remove.('classname')
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username);
  paintGreetings(username);
}

function paintGreetings(username) {
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  paintGreetings(savedUsername);
}
/* 
submit 는 엔터를 누르거나 버튼을 클릭할 때 발생
addEventListener를 추가할 때 onLoginBtnSubmit에 ()를 붙이지 않는데 ()는
function을 '즉시' 실행하며 한 번만 실행한다는 뜻.
addEventListener는 우리가 지정한 이벤트가 발생했을 때만 브라우저가 실행시키기 위해 쓰는 것.
*/
