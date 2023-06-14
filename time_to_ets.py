import time
from win10toast import ToastNotifier
import requests

def get_time_left():
	ets_leave = 1688018400
	current_time = time.time()
	total_sec = ets_leave - current_time
	minutes = int(total_sec) / 60
	leftover_min = int(minutes) % 60
	hours = int(minutes)/60
	leftover_hours = int(hours) % 24
	days = int(hours)/24
	final = f'{int(days)} days, {int(leftover_hours)} hours, and {int(leftover_min)} minutes to FREEDOM!'
	return final

def check_if_noon():
	hour = time.asctime().split()[3]
	if hour == "12:00:00":
		return True

def send_notifications():
	#windows notification
	print("***Sending windows notification***")
	toast = ToastNotifier()
	final = get_time_left()
	toast.show_toast(
		"Time until ETS",
		final,
		duration = 20,
		icon_path = ".\\download.ico",
		threaded = True,
		)
	#android notification
	print("***Sending telegram message***")
	id = "6218744091"
	token = "6012387725:AAFOgyxlgmyxZ-4vJVwPIzF6Q7UfhrB7SKw"
	url = f"https://api.telegram.org/bot{token}/sendMessage"
	params = {"chat_id": id, "text": final}
	r = requests.get(url=url,params=params)

#use this if running in terminal in background
def main1():
	print("Program start...")
	while True:
		if check_if_noon():
			send_notifications()
#use this if running as scheduled task
def main2():
	send_notifications()
	exit()

if __name__ == "__main__":
	main2()