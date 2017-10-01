# Importar librerias necesarias

import RPi.GPIO as GPIO
import time

# Configurar las variables

GPIO.setmode(GPIO.BCM)

	# Puertos GPIO con nombre

Eco = 21 # Entrada de captura de eco
Trig = 20 # Salida de sonido
Off = 17  # Detener el loop
PWM = 18
M1 = 27
M2 = 22

x = 20
y = 5

# Configuracion de los puertos

GPIO.setup(Eco,GPIO.IN)
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Off, GPIO.IN)
GPIO.setup(PWM, GPIO.OUT)
GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)

# Configurar puerto PWM

PWM = GPIO.PWM(PWM,100)  # una senal PWM, 100 pulsos por segundo

# Inicializar

GPIO.output(Trig, False)
PWM.start(x)

# Loop infinito

while (GPIO.input(Off) == GPIO.LOW):

	GPIO.output(Trig,True)
	time.sleep(0.0001)
	GPIO.output(Trig,False)
	start = time.time()
	while GPIO.input(Eco) == 0:
		start = time.time()
	while GPIO.input(Eco) == 1:
		stop = time.time()
	dif = stop - start
	distancia = (dif*34300)/2
	
	# Control motor a distancia de 6 cm
	if distancia > 6: # Si es mayor se aleja
		GPIO.output(M1, GPIO.LOW)
		GPIO.output(M2,GPIO.HIGH)

	if distancia < 6: # Si es menor se acerca
		GPIO.output(M1,GPIO.HIGH)
		GPIO.output(M2,GPIO.LOW)
	
	print distancia
	time.sleep (0.05)
# Fin de programa
GPIO.cleanup()
