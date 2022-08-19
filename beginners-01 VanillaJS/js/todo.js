const toDoForm = document.getElementById("todo-form");
const toDoInput = document.querySelector("#todo-form input");
const toDoList = document.getElementById("todo-list");

const TODOS_KEY = "todos";

let toDos = [];

function saveToDos() {
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
  // JSON.stringify( -- ) -> object를 string으로 바꿔줌
  //배열을 문자열로 JSON.stringify  문자열을 오브젝트로 JSON.parse
  // localStorage에 저장할 때 array는 저장할 수 없기 떄문에.
}

function deleteToDo(event) {
  const li = event.target.parentElement;
  li.remove();
  toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
  // parselnt() 문자열을 숫자로 변환
  saveToDos();
}

function paintToDo(newTodo) {
  const li = document.createElement("li");
  li.id = newTodo.id;
  const span = document.createElement("span");
  span.innerText = newTodo.text;
  const button = document.createElement("button");
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
}

function handleToDoSubmit(event) {
  event.preventDefault();
  const newTodo = toDoInput.value;
  // toDoInput의 현재 value를 새로운 변수에 복사
  toDoInput.value = "";
  // 그 후에 toDoInput의 value를 가지고 무엇을 하든 newTodo에는 아무 영향 X
  const newTodoObj = {
    text: newTodo,
    id: Date.now(), // 밀리초(1000분의 1초)를 주는 함수
  };
  toDos.push(newTodoObj);
  // 여기서 DB로 매번 사용자가 적어둔 Obj를 toDos arry로 push
  paintToDo(newTodoObj);
  saveToDos();
}

toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos !== null) {
  const parsedToDos = JSON.parse(savedToDos);
  // parsedToDos.forEach((item) => console.log("this is the turn of ", item));
  toDos = parsedToDos;
  parsedToDos.forEach(paintToDo);
}
// forEach(func.) : array의 각 item에 대하여 func.를 실행한다.
// forEach( (item) => console.log(item) )
// array의 각 요소를 item이라고 하고, console.log(item)을 실행
