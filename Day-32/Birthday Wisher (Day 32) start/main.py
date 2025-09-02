import smtplib
import datetime as dt
import random

now = dt.datetime.now()
my_email = "rpa.prashant.test@gmail.com"
password = "yinzfoojxtousfrp"

def send_quote(quote):
    global my_email, password
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rpa.prashant@yahoo.com", msg=f"Subject:Monday quote\n\n{quote}")

def get_random_quote():
    with open("quotes.txt", "r") as f:
        lines = f.readlines()
        return lines[random.randint(0,len(lines))]

if dt.date.weekday(dt.datetime.now())==6:
    quote = get_random_quote()
    send_quote(quote)
    print("Mail sent")
else:
    print(dt.date.weekday(dt.datetime.now()))