import requests


def send_sms(phone):
    response = requests.get(f'https://sms.ru/code/call?phone={phone}&api_id=889303E4-8329-EC51-0FB8-1085C296D2AC')
    print(response.text)
    if response.status_code == 200:
        if response.json()["status"] == 'OK':
            code = response.json()['code']
            return [1, code]
        else:
            return [0, f'Ошибка, {response.json()["status"]}']
    else:
        return [0, 'Ошибка!']


print(send_sms('79151290127'))
