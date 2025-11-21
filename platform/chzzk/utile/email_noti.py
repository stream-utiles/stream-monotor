import smtplib
import orjson
import os

file_path = os.path.abspath(__file__)
utile_path = os.path.dirname(file_path)
chzzk_path = os.path.dirname(utile_path)
json_path = os.path.join(chzzk_path, 'config.json')

with open(json_path, "rb") as f:
    config = orjson.loads(f.read())


ID = config["email"]["id"]
PW = config["email"]['pw']

def email(title, context, target_email=ID, sender_email=ID, sender_password=PW):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            message = f"Subject: {title}\n\n{context}"
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=target_email,
                msg=message.encode('utf-8')  # 한글 포함 시 인코딩
            )
        print("✅ 이메일 전송 성공!")
    except Exception as e:
        print(f"❌ 이메일 전송 실패: {e}")

email('asd', 'asd')