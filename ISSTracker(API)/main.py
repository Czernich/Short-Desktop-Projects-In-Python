import requests
from datetime import datetime
from time import sleep
import smtplib

MY_EMAIL = "MY@EMAIL.COM"
PASSWORD = "PASSWORD123"
MY_LAT = 51.953941
MY_LONG = 20.147141
current_day = datetime.now()
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


def is_iss_overhead():

    # Getting current position of ISS
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        print("ISS is above your head")
        return True
    else:
        return False


def is_night():

    # Getting time of sunrise and sunset
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    sunrise_time = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 1
    sunset_time = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 1

    if current_day.hour <= sunset_time or current_day.hour >= sunrise_time:
        return True


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="MY@EMAIL.COM",
            msg="Subject:Look Up!\n\n ISS is above your head!")


while True:
    sleep(60)
    if is_iss_overhead() and is_night():
        send_email()
