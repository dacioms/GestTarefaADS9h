from datetime import datetime

def isDateValid(data):
    try:
        data = datetime.strptime(data, '%d-%m-%Y')
        return True
    except ValueError:
        return False




data = input('Informe a data de término da terefa: ')
print(isDateValid(data))


def isDateValid(data):
    try:
        data = datetime.strptime(data, '%d-%m-%Y')
        return True
    except ValueError:
        return False