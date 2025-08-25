from pystyle import Colors, Colorate, Center, Write, System, Box, Banner

print(Banner.Lines("[+] Abood"))

Write.Print('[-] this us foer cslculater\n', Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube('program'))

while True:
    while True:
        number1 = int(Write.Input('[+] write first number : ', Colors.blue_to_green, interval=0.1))
        operator = Write.Input('[+] choose operator (+, -, *, /) : ', Colors.blue_to_green, interval=0.1)
        number2 = int(Write.Input('[+] write second number : ', Colors.blue_to_green, interval=0.1))

        if operator == '+':
            Write.Print('[+] the result is : ', Colors.green, interval=0.1)
            print(number1 + number2)
            break
        elif operator == '-':
            Write.Print('[+] the result is : ', Colors.green, interval=0.1)
            print(number1 - number2)
            break
        elif operator == '*':
            Write.Print('[+] the result is : ', Colors.green, interval=0.1)
            print(number1 * number2)
            break
        elif operator == '/':
            Write.Print('[+] the result is : ', Colors.green, interval=0.1)
            print(number1 / number2)
            break
        else:
            Write.Print('[-] please write just : + - * /', Colors.red, interval=0.1)
