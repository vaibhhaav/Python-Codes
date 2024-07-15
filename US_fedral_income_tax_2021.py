# Ask user for income and calculate US Fedral Income Tax for 2021
def main():
    income = int(input('Enter 2021 income: '))
    if income <= 9875:
        tax = income * 0.1
        bracket = "10%"
    elif income <= 40125:
        tax = 987.5 + (income - 9875) * 0.12
        bracket = '12%'
    elif income <= 85525:
        tax = 4617.5 + (income - 40125) * 0.22
        bracket = '22%'
    elif income <= 16330:
        tax = 14605.5 + (income - 85525) * 0.24
        bracket = '24%'
    else:
        tax = 33271.5 + (income - 163300) * 0.32
        bracket = '32%'
    
    print('An income of', income,'places you in the ', bracket, 'income bracket')
    print('The US Fedral tax on an income of', income,'is', tax)

main()