const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
// context( = ctx)는 기본적으로 붓(브러쉬)

canvas.width = 800;
canvas.height = 800;
ctx.lineWidth = 2;

const colors = [
  "#55efc4",
  "#81ecec",
  "#74b9ff",
  "#a29bfe",
  "#b2bec3",
  "#e17055",
  "#fdcb6e",
  "#00cec9",
];

function onClick(event) {
  ctx.beginPath();
  ctx.moveTo(400, 400);
  const color = colors[Math.floor(Math.random() * colors.length)];
  ctx.strokeStyle = color;
  ctx.lineTo(event.offsetX, event.offsetY);
  ctx.stroke();
}

canvas.addEventListener("mousemove", onClick);
/*
canvas에서 그림을 그릴 때는 단계별로 진행 필요
그린 그림들의 경로를 나눌 수 있음
    새 경로 시작하기: beginPath()
    
    moveTo(x, y); -> 브러쉬의 좌표를 움직여줌(어디서부터 그릴지 위치 선정)
    lineTo(x, y) -> 라인을 그려줌(그림 그리기)
라인이 끝난 점이 다음에 시작하는 브러쉬 좌표이다
    fillRect = fill + Rect = fill + (moveTo + lineTo)
*/
