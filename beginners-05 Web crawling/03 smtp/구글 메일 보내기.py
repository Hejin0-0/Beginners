import smtplib
from email.mime.text import MIMEText

sendEmail = "@gmail.com"
recvEmail = "받는 이메일"
password = "구글 비밀번호"

smtpName = "smtp.gmail.com"  # smtp 서버 주소
smtpPort = 587  # smtp 포트 번호

text = "매일 내용"
msg = MIMEText(text)  # MIMEText(text , _charset = "utf8")

msg["Subject"] = "이것은 메일제목"
msg["From"] = sendEmail
msg["To"] = recvEmail
print(msg.as_string())

s = smtplib.SMTP(smtpName, smtpPort)  # 메일 서버 연결
s.starttls()  # TLS 보안 처리
s.login(sendEmail, password)  # 로그인
s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환해야 합니다.
s.close()  # smtp 서버 연결을 종료합니다.

# 에러가 날 경우
# [구글 계정 설정] - [보안] - [보안 수준 낮은앱 액세스] - [허용]을 해주면 위 코드가 실행
