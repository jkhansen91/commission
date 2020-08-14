# This function checks inputs to make sure they are valid percentages
def checkPercent(percent):
    # If the input string is not completely numeric, error prints
    if not percent.isnumeric():
        print('Please enter a number and omit "%" sign:')
        return False
    else:
        percent = int(percent)
        # If the input string is over 100 or less than zero, error prints
        if percent >= 100 or percent <= 0:
            print("Please enter a valid percentage:")
            return False
        else:
            return True

# This is the goal commission that the user inputs
print('Goal commission: ')
commission = int(input())

# The gross commission percentage is how much of the house sale goes to the firm
print('Gross commission percentage: ')
while True:
    grossPercent = input()
    if checkPercent(grossPercent):
        break

# The commission split is the percentage of the gross commission that the firm pays out to the agent
print('Commission split (for agent): ')
while True:
    agentSplit = input()
    if checkPercent(agentSplit):
        break

# Calculates the gross commission and the total dollar amount to be sold
grossCommission = int(commission / (int(agentSplit) / 100))
houseSales = int(grossCommission / (int(grossPercent) / 100))

# Formats both of these numbers to include commas every 3 digits, for ease of reading
grossCommission = "{:,}".format(grossCommission)
houseSales = "{:,}".format(houseSales)

# Prints results
print('Gross commission goal is: ' + grossCommission)
print('Total sales goal is: ' + houseSales)

