#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
import random
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()
obtr = ObjectTracker()

color_sensor = ColorSensor(INPUT_1)
ultra_frente = UltrasonicSensor(INPUT_2)
ultra_esquerda = UltrasonicSensor(INPUT_3)
ultra_direita = UltrasonicSensor(INPUT_4)
gyro_sensor_in5 = GyroSensor(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts
def main():
    tempo = time.time()
    
    while True:
        if (color_sensor.color == 5): #código para vermelho no ev3
            tempo = time.time()
            tank_drive.on(left_speed = -100, right_speed = -100)
            time.sleep(1)
            tank_drive.off()
            tank_drive.on(left_speed = 50, right_speed = -50)
            time.sleep(1)
            tank_drive.off()
            if (color_sensor.color == 5): #se continuar na borda recua mais
                tank_drive.on(left_speed = -70, right_speed = -70)
                time.sleep(0.5)
                tank_drive.off()
            
        #distância do obstáculo detectado em cada sensor
        dist_frente = ultra_frente.distance_centimeters
        dist_esquerda = ultra_esquerda.distance_centimeters
        dist_direita = ultra_direita.distance_centimeters
        
        direcao, found = seguir_obstaculo(dist_frente, dist_esquerda, dist_direita)
        
        if found:
            tempo = time.time()
        
        if (direcao == 'front'):
            tank_drive.on(left_speed = 70, right_speed = 70)
        elif (direcao == 'left'):
            tank_drive.on(left_speed = -50, right_speed = 50)
        else:
            tank_drive.on(left_speed = 50, right_speed = -50)
            
        time_now = time.time()
        
        if ((time_now - tempo) > 6):
            tank_drive.on(left_speed = 50, right_speed = -50)
            time.sleep(1)
            tank_drive.off()
            tank_drive.on(left_speed = 70, right_speed = 70)
            tempo = time.time()
        
#vai em direção ao obstáculo mais perto
def seguir_obstaculo(a, b, c):
    direcoes = {'front': a,
        'left': b,
        'right': c}
    
    if all(distancias > 30 for distancias in direcoes.values()):
        return 'front', False
        
    alvo = min(direcoes, key = direcoes.get)
    return alvo, True
        
        
main()
