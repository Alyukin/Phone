alfabet = 'abcdefghijklmnopqrstuvwxyz'


def encryptMessage(Message):
    encryptedMessage = ''

    for letter in Message:
        place = alfabet.find(letter)
        newPlace = (place + 1 + len(alfabet)) % len(alfabet)

        if letter in alfabet:
            encryptedMessage += alfabet[newPlace]
        else:
            encryptedMessage += letter
            
    return encryptedMessage
