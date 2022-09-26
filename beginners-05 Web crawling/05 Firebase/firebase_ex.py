import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate(
    "/Users/lovenstein/Documents/Python/web crawling/05 Firebase/myKey.json"
)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://semicircle-53f7f.firebaseio.com/"}
)
"""
ref = db.reference()  # db 위치 지정
ref.update({"Munchen": "빼꼼"})  # 해당 변수가 없으면 생성한다.

ref = db.reference("강좌/파이썬")  # 경로가 없으면 생성한다.
ref.update({"파이썬 레시피 웹 활용": "complete"})
ref.update({"파이썬 괴식 레시피": "Proceeding"})

# 리스트 전송시
ref = db.reference()  # db 위치 지정
ref.update({"Bear": ["반달가슴곰", "북극곰", "판다", "피즐리"]})  # 해당 변수가 없으면 생성한다.
"""

# 데이터베이스 레퍼런스 생성 후 데이터 읽기
ref = db.reference("없는 경로")  # 이 당시의 데이터가 확인된다.
print(ref.get())  # 특정값이 가져와지거나

ref = db.reference("Munchen")
print(ref.get())

ref = db.reference("강좌/파이썬")
print(ref.get())  # json형태로 받아와 진다.

ref = db.reference("수강자")
print(ref.get())  # list로 반환
