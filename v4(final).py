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
gyro = GyroSensor(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts
def main():
    gyro.reset()
    time.sleep(0.5)
    tempo = time.time()
    
    while True:
        check_borda(tempo)
        
        if (ultra_frente.distance_centimeters < 30):
            steering_drive.on(steering = 0, speed = 70)
            tempo = time.time()
        elif (ultra_esquerda.distance_centimeters < 30):
            steering_drive.on(steering = -50, speed = 70)
            tempo = time.time()
        elif (ultra_direita.distance_centimeters < 30):
            steering_drive.on(steering = 50, speed = 70)
            tempo = time.time()
        else:
            steering_drive.on(steering = 0, speed = 70)
            
        time_now = time.time()
        
        if ((time_now - tempo) > 6):
            girar(90, 70)
            tempo = time.time()
        
def check_borda(tempo):
    if (color_sensor.color == 5):
        steering_drive.off()
        girar(90, 70)
    time.sleep(0.1)
    if (color_sensor.color == 5):
        girar(90, 70)
    else:
        steering_drive.on_for_seconds(steering=0, speed=70, seconds=0.3)
    tempo = time.time()

def girar(alpha, velocidade):
    beta = gyro.angle
    alvo = beta + alpha
    steering_drive.on(steering = 100, speed = velocidade)
    while (gyro.angle < alvo):
        if (color_sensor.color == 5):
            steering_drive.off()
            steering_drive.on_for_seconds(steering = 0, speed = -100, seconds = 1)
            girar(90, velocidade)
        time.sleep(0.01)
    steering_drive.off()
        
main()
