from pyfirmata import Arduino, OUTPUT

PORTA = 'COM7'

arduino = Arduino(PORTA)
arduino.digital[13].mode = OUTPUT

while True:
    arduino.digital[13].write(1)
    arduino.pass_time(0.5)
    arduino.digital[13].write(0)
    arduino.pass_time(0.5)
