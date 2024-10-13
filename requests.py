import requests

api_url='http://api.open-notify.org/iss-now.json'
responce=requests.get(api_url) #Отправка get запроса и сохранение в респонсе

if responce.status_code== 200: #если ответ на запрос 200 то смотрим что пришло
    print(responce.text)
else:
    print(responce.status_code) # при другом ответе выводим код