from pyfirmata import Arduino, OUTPUT

PORTA = 'COM7'

arduino = Arduino(PORTA)
arduino.digital[13].mode = OUTPUT

try:
    while True:
        estado = input('Digite 1 para ligar e 0 para desligar: ')
        if(estado =='1' or estado == '0'):
            arduino.digital[13].write(int(estado))
        else:
            print('O valor digitado é inválido')    
except KeyboardInterrupt:
    print('O valor digitado é inválido')    
    arduino.exit()