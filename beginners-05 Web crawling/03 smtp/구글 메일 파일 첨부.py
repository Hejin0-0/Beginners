import smtplib  # 메일을 보내기 위한 라이브러리 모듈
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sendEmail = "구글ID@gmail.com"
recvEmail = "받는 이메일"
password = "구글 비밀번호"

smtpName = "smtp.gmail.com"
smtpPort = 587

# 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
msg = MIMEMultipart()

msg["Subject"] = "메일 제목"
msg["From"] = sendEmail
msg["To"] = recvEmail

# 본문 추가
text = "이것은 메일 내용"
contentPart = MIMEText(text)  # MIMEText(text , _charset = "utf8")
msg.attach(contentPart)

# 파일 추가
etcFileName = "파일명"
with open(etcFileName, "rb") as etcFD:
    etcPart = MIMEApplication(etcFD.read())
    # 첨부파일의 정보를 헤더로 추가
    etcPart.add_header("Content-Disposition", "attachment", filename=etcFileName)
    msg.attach(etcPart)

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.close()
