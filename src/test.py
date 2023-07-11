from datetime import datetime, timedelta

today = datetime(2022, 7, 10)
current_week_start = today - timedelta(days=today.weekday())
previous_week_start = current_week_start - timedelta(days=7)
previous_week_end = current_week_start - timedelta(days=1)

saturday_previous_week = previous_week_start + timedelta(days=5)
friday_current_week = current_week_start + timedelta(days=4)

print(f"Сегодня - {today}")
print(f"Прошлая суббота - {saturday_previous_week}")
print(f"Текущая пятница - {friday_current_week}")