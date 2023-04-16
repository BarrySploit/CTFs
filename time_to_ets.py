import time
from win10toast import ToastNotifier

ets_leave = 1688968800.0000000
current_time = time.time()
total_sec = ets_leave - current_time
minutes = int(total_sec) / 60
leftover_min = int(minutes) % 60
hours = int(minutes)/60
leftover_hours = int(hours) % 24
days = int(hours)/24
final = f'{int(days)} days, {int(leftover_hours)} hours, and {int(leftover_min)} minutes to FREEDOM!'
toast = ToastNotifier()
while True:
	toast.show_toast(
		"Time until ETS",
		final,
		duration = 20,
		icon_path = "C:\\users\\trans\\Downloads\\download.ico",
		threaded = True,
	)
	time.sleep(600)