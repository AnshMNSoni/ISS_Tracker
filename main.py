# ISS Tracker

import requests
import datetime as dt
import smtplib as st


response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

iss_lat = data['iss_position']['latitude']
iss_lng = data['iss_position']['longitude']

MY_LAT = 20.946701
MY_LNG = 72.952034


parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(url=' https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]


now = dt.datetime.now()
current_time = now.hour

if (current_time >= float(sunset) and float(iss_lng) - 5 <= MY_LAT <= float(iss_lat) + 5 and float(iss_lng) - 5 <= MY_LNG <= float(iss_lng) + 5):
    my_mail = 'anshsoni702@gmail.com'
    password = 'hnae syae ioqr rney'
    
    with st.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs='anshsoni702@gmail.com', msg=f"Subject:ISS LOCAION\n\nISS is near to your current location.")