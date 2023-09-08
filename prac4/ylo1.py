from typing import Dict
from import_this import RACE_DATA

a = 1

for racer_id, racer_info in RACE_DATA.items():
    if a <= 3:
        if racer_info['FinishedPlace'] == a:
            print("Имя гонщика:", racer_info['RacerName'])
            print("Название команды:", racer_info['RacerTeam'])
            print("Занятое место:", racer_info['FinishedPlace'])
            print("Время заезда (в секундах):", racer_info['FinishedTimeSeconds'])
            print()
        a += 1
    else:
        break