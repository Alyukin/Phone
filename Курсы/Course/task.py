from functions import encryptMessage

realResult = encryptMessage('abc')
expectedResult = ('bcd')

print('Кейс должет вернуть результат значение истины для простого преобразования цезаря:', realResult == expectedResult)
