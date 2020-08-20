import requests #импортируем модуль
def get_text():
    send=requests.post('https://neurovolk.xyz') #делаем запрос
    file = open('test.html','w') #создаем файл для записи результатов
    file.write(send.text) #записываем результат
    file.close() #закрываем файл
    with open('test.html', 'r') as f:#открваем скачанный html
        nums = f.read().splitlines() #сохраняем в переменную
    test = nums[20] #обрезка до нужной строки
    a = test[test.find(">") + 1 : ] #обрезка с начала
    b = '<'.join(a.split('<')[:-3])#обрезка с конца
    return b#возвращение полученной цитаты
