#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
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

color_sensor_in1 = ColorSensor(INPUT_1)
ultra_frente = UltrasonicSensor(INPUT_2)
ultra_esquerda = UltrasonicSensor(INPUT_3)
ultra_direita = UltrasonicSensor(INPUT_4)
gyro_sensor_in5 = GyroSensor(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts
def main():
    while True:
        #distância do obstáculo detectado em cada sensor
        dist_frente = ultra_frente.distance_centimeters
        dist_esquerda = ultra_esquerda.distance_centimeters
        dist_direita = ultra_direita.distance_centimeters
        
        direcao = seguir_obstaculo(dist_frente, dist_esquerda, dist_direita)
        
        if (direcao == 'front'):
            tank_drive.on(left_speed = 100, right_speed = 100)
        elif (direcao == 'left'):
            tank_drive.on(left_speed = -50, right_speed = 50)
        else:
            tank_drive.on(left_speed = 50, right_speed = -50)
            
#vai em direção ao obstáculo mais perto
def seguir_obstaculo(a, b, c):
    direcoes = {'front': a,
        'left': b,
        'right': c}
    alvo = min(direcoes, key = direcoes.get)
    return alvo
        
main()
