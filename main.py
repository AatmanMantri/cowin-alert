from datetime import datetime
from playsound import playsound
import requests
import sys
import time

payload = {}
headers = {
    'authority': 'cdn-api.co-vin.in',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'origin': 'https://www.cowin.gov.in',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cowin.gov.in/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"897-FVcRBiLjpfwbJ4dOo9LPcxEvYko"'
}


def get_data(pincode):
    date = datetime.today().strftime('%d-%m-%Y')
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pincode + "&date=" + date
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        response = response.json()
        return True, response
    else:
		print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), '- Status code =', response.status_code)
        return False, None


def check_slot_availability(response):
    if len(response['centers']) > 0:
        centers = response['centers']
        for center in centers:
            sessions = center['sessions']
            for session in sessions:
                age_limit = session['min_age_limit']
                available = session['available_capacity']
                vaccine = session['vaccine']
                if age_limit == 18 and available > 0:
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), '-', vaccine)
                    return True
	print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), '- slot not available')
    return False


if __name__ == '__main__':
    args = sys.argv
    pincode = args[1]
    refresh_time = int(args[2])
    alert_song = args[3]
    while True:
        success, response = get_data(pincode)
        if success:
            availability = check_slot_availability(response)
            if availability:
                break
        time.sleep(refresh_time)
    playsound(alert_song)
