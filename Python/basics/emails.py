import smtplib
import email
from email.header import decode_header

sender_email = "your_email@example.com"
receriver_email = "receiver@example.com"
password = "123"

subject ="x"
body= "this is the body"

message = "subject etc"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receriver_email, message)
    print("sent")

# parsing
raw_email = b"raw_email_data_here"

msg=email.message_from_bytes(raw_email)

subject, encoding = decode_header(msg["Subject"])[0]
if isinstance(subject, bytes):
    subject = subject.decode(encoding if encoding else "utf-8")
print(subject)

print(msg.get("From"))

if msg.is_multipart():
    for part in msg.walk():
        content_type = part.get_content_type()
        if content_type == "text/plain":
            body = part.get_payload(decode=True).decode()
            print(body)
else:
    body = msg.get_payload(decode=True).decode()
    print(body)
