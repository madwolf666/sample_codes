import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('メールの本文です。')  # MIMETextオブジェクトでメッセージを組み立てる。
msg['Subject'] = Header('メールの件名', 'utf-8')  # 件名に日本語を含める場合はHeaderオブジェクトを使う。
msg['From'] = 'madwolf666@live.jp'  # 差出人のメールアドレス
msg['To'] = 'madwolf666@live.jp'  # 送信先のメールアドレス
#msg['From'] = 'me@example.com'  # 差出人のメールアドレス
#msg['To'] = 'you@example.com'  # 送信先のメールアドレス

with smtplib.SMTP('smtp.gmail.com') as smtp:  # SMTP()の第1引数にSMTPサーバーのホスト名を指定する。
    smtp.login('madwolf666','chappy666')
    smtp.send_message(msg)  # メールを送信する。
