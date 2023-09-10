time_seconds = int(input())
time_hours = time_seconds // 3600
time_minutes = (time_seconds % 3600) // 60
time_seconds = time_seconds % 60
time_formatted = f"{time_hours:02d} час(а / ов), {time_minutes:02d} минут (а / ы)"
print("Время:", time_formatted)