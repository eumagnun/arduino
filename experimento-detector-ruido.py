from pyfirmata import Arduino, OUTPUT, util

PORTA = 'COM7'
LIMITE_CAPTURA_SOM = 0.650

arduino = Arduino(PORTA)
arduino.digital[13].mode = OUTPUT
it = util.Iterator(arduino)
it.start()
arduino.analog[0].enable_reporting()

try:
    while True:

        valor = arduino.analog[0].read()
        if valor and valor > LIMITE_CAPTURA_SOM:
            print(valor)
            arduino.digital[13].write(int(1))
        else:
            print(valor)
            arduino.digital[13].write(int(0))
except KeyboardInterrupt:
    arduino.exit()

