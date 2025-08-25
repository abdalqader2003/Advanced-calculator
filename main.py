from pystyle import *

print(Box.Lines('[+] Abood'))
Write.Print('[-]this program for calculator \n',Colors.purple_to_red, interval =0.1)
Write.Print('[-]Write username and password \n\n ',Colors.purple_to_red, interval =0.1)

print (Box.DoubleCube('Example[1]'))
while True :
    username = Write.Input('- write username :',Colors.blue_to_green,interval =0.1)
    password = Write.Input('- write password :',Colors.blue_to_green,interval =0.1)
    if username == 'abood'and password == '123456':

        input('press any key to exit')
    else:
        write.print('[+] welcome admin \n', Colors.green, interval=0.2)


