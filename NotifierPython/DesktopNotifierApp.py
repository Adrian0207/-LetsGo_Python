import datetime
import time
import requests

from plyer import notification

def notifyMe():
    url = "https://rapidapi.p.rapidapi.com/headstails"
    headers = {
        'x-rapidapi-host': "coin-flip1.p.rapidapi.com",
        'x-rapidapi-key': "7a7085323fmshea59ec170adedfbp1cc859jsn773757deebd0"
    }
    response = None

    try:
        response = requests.request("GET", url, headers=headers)
    except:
        print("Please! Check your internet connection")

    if response != None:
        data = response.json()['outcome']

        while True:
            
            notification.notify(
                title='Heads/Tails', 
                message='The coin flip: {}'.format(data), 
                app_name='FlipCoin', 
                app_icon='C:\\Users\\evere\\Desktop\\NotifierPython\\coin.ico', 
                timeout=10, 
                toast=False
            )
            time.sleep(60*1)

notifyMe()

