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

color_sensor = ColorSensor(INPUT_1)
ultra_frente = UltrasonicSensor(INPUT_2)
ultra_esquerda = UltrasonicSensor(INPUT_3)
ultra_direita = UltrasonicSensor(INPUT_4)
gyro = GyroSensor(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts
def main():
    tempo = time.time()
    
    while True:
        angulo_now = gyro.angle
        bordas = []
        if (color_sensor.color == 5 or next_borda(bordas, angulo_now) == True): #código para vermelho no ev3
            tempo = time.time()
            bordas.append(angulo_now)
            tank_drive.off()
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
            if (dist_frente < 15):
                desacelerar(70, 3, 10)
            else:
                tank_drive.on(left_speed = 70, right_speed = 70)
        elif (direcao == 'left'):
            tank_drive.on(left_speed = -50, right_speed = 50)
        else:
            tank_drive.on(left_speed = 50, right_speed = -50)
            
        time_now = time.time()
        
        if is_preso(dist_frente, dist_esquerda, dist_direita):
            tank_drive.on(left_speed = 70, right_speed = 70)
            time.sleep(1)
            
        
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
    
    if all(distancias > 40 for distancias in direcoes.values()):
        return 'front', False
        
    alvo = min(direcoes, key = direcoes.get)
    return alvo, True

#verificar se o robô ficou preso entre obstáculos mt próximos
def is_preso(a, b, c):
    distancias = [a, b, c]
    count = 0
    for distancia in distancias:
        if (distancia < 20):
            count += 1
            if (count == 2):
                return True
    return False
    
def desacelerar(v0, tempo, incremento):
    
    while (time.time() < tempo):
        tank_drive.on(left_speed = vo, right_speed = vo)
        time.sleep(0.1)
        vo -= incremento
        
def next_borda(list, angulo):
    for item in list:
        if (abs(item - angulo) < 20):
            return True
    return False
        
main()
