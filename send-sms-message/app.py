import requests
import schedule
import time

def send_sms_message():
    try:
        resp = requests.post('https://textbelt.com/text', {
            'phone': '+2349031389842',  
            'message': 'Sending SMS message with Python',
            'key': 'textbelt',      
        })
        data = resp.json()
        print(data)

        if data.get("success"):
            print("SMS sent successfully!")
        else:
            print("Failed to send:", data.get("error"))

    except Exception as e:
        print("Error:", e)

# Schedule every 5 seconds
schedule.every(5).seconds.do(send_sms_message)

while True:
    schedule.run_pending()
    time.sleep(1)
