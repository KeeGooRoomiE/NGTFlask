import json
from datetime import datetime, timedelta

a = {
    "result": {
        "code": "Success",
        "description": "Сроки действия баллов получены"
    },
    "data": {
        "bonus_valid": [
            {
                "valid": "2024-10-14T00:00:00",
                "points": 41
            },
            {
                "valid": "2024-10-27T00:00:00",
                "points": 33
            }
        ]
    }
}
print(json.dumps(a))
data = a["data"]
week_points = 0
month_points = 0
if len(data)>0 and "bonus_valid" in data:

    valid_bonuses = data["bonus_valid"]

    for points in valid_bonuses:
        if datetime.fromisoformat(points["valid"])-datetime.now()<=timedelta(days=7):
            week_points=week_points+points["points"]
        if datetime.fromisoformat(points["valid"])-datetime.now()<=timedelta(days=30):
            month_points=month_points+points["points"]
