#ЭТО ТЕСТ С ТЕМ САМЫМ sorted, оставляю, чтобы не забыть

from typing import Dict
from import_this import RACE_DATA

def get_plce(zanyatoe_mesto):
    return zanyatoe_mesto[1].get('FinishedPlace')

sorted_data = sorted(RACE_DATA.items(), key=get_plce)

for racer_id, racer_info in sorted_data[:3]:
    if racer_info['FinishedPlace'] == 1:
        print(f"Выиграл - {racer_info['RacerName']}, поздравляем!")
    print("Имя гонщика:", racer_info['RacerName'])
    print("Название команды:", racer_info['RacerTeam'])
    print("Занятое место:", racer_info['FinishedPlace'])
    print("Время заезда (в секундах):", racer_info['FinishedTimeSeconds'])
    print()