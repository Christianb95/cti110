# CTI-110 P2HW1- Basic Math
# Christian Barreto
# 2-4-2020

def main():
    #INPUT
    results = 0

    # Ask user for 1st number & store input
    num1 = int(input('What is your first number?'))

    # Ask user for 2nd number & Store input
    num2 = int(input('What is your second number?'))

    #PROCESS
    # Add num1 and num2 & store sum
    mathSum = num1 + num2

    # Multiply num1 and num2 & store result
    results = num1 * num2

    #OUTPUT
    #Display num1, num2, sum, and result
    print('Users first number: ', num1)
    print('Users second number: ', num2)
    print('Sum of numbers: ', mathSum)
    print('Result of numbers: ', results)

main()
