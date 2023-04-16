import time
from win10toast import ToastNotifier
import requests


ets_leave = 1688968800.0000000
current_time = time.time()
total_sec = ets_leave - current_time
minutes = int(total_sec) / 60
leftover_min = int(minutes) % 60
hours = int(minutes)/60
leftover_hours = int(hours) % 24
days = int(hours)/24
final = f'{int(days)} days, {int(leftover_hours)} hours, and {int(leftover_min)} minutes to FREEDOM!'
#windows notification
print("Sending windows notification")
toast = ToastNotifier()
while True:
	toast.show_toast(
		"Time until ETS",
		final,
		duration = 20,
		icon_path = ".\\download.ico",
		threaded = True,
	)

#android notification
print("sending telegram message")
id = "6218744091"
token = "6012387725:AAFOgyxlgmyxZ-4vJVwPIzF6Q7UfhrB7SKw"
url = f"https://api.telegram.org/barry_ets_bot{token}/sendMessage"
params = {"chat_id": id, "text": final}
r = requests.get(url=url,params=params)
time.sleep(60)