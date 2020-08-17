def written_percent(percent):
    valid_percent = ''
    for char in percent:
        if char != '%':
            valid_percent += char
    valid_percent = int(valid_percent)
    return valid_percent


def decimal_percent(percent):
    print('Assuming percentage passed as decimal. Multiplying by 100 for value')
    percent *= 100
    return int(percent)


def convert_percent(percent):
    if '%' in percent:
        percent = written_percent(percent)
    else:
        percent = float(percent)
        if percent < 1:
            percent = decimal_percent(percent)
        else:
            percent = int(percent)
    return percent


def checkPercent(message):
    percent = input(message)
    valid = True
    try:
        percent = int(percent)
    except ValueError:
        try:
            percent = convert_percent(percent)
        except ValueError:
            print('Percentages must be a number.')
            return False, 0

    if percent > 100:
        print('Percent cannot be over 100')
        valid = False

    return valid, percent


def calcuation(commission, percentage):
    return int(commission / (percentage / 100))


commission = None
while not isinstance(commission, int):
    try:
        commission = int(input('Goal comission:\n'))
    except ValueError:
        print('Goal comission must be a whole integer value')


valid_gross_percent = False
while not valid_gross_percent:
    valid_gross_percent, grossPercent = checkPercent('Gross commission percentage:\n')

valid_commmission = False
while not valid_commmission:
    valid_commmission, agentSplit = checkPercent('Commission split (for agent):\n')

grossCommission = calcuation(commission, agentSplit)
houseSales = calcuation(grossCommission, grossPercent)

print(f'Gross commission goal is: {grossCommission:,}')
print(f'Total sales goal is: {houseSales:,}')
