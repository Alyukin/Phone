from functions import encryptMessage

Message = input('Введите текст для шифрования:')

encryptedMessage = encryptMessage(Message)
print(encryptedMessage)