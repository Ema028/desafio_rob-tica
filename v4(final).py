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
    tempo = time.time()
    
    while True:
        check_borda(tempo)
        
        if (ultra_frente.distance_centimeters < 30):
            steering_drive.on(steering = 0, speed = 70)
            tempo = time.time()
        elif (ultra_esquerda.distance_centimeters < 30):
            steering_drive.on(steering = -50, speed = 70)
            check_borda(tempo)
            tempo = time.time()
        elif (ultra_direita.distance_centimeters < 30):
            steering_drive.on(steering = 50, speed = 70)
            check_borda(tempo)
            tempo = time.time()
        else:
            steering_drive.on(steering = 0, speed = 70)
            
        time_now = time.time()
        
        if ((time_now - tempo) > 6):
            steering_drive.on_for_seconds(steering = 0, speed = -100, seconds = 1)
            steering_drive.on_for_seconds(steering = 100, speed = 70, seconds = 1)
            check_borda(tempo)
            tempo = time.time()
        
def check_borda(tempo):
    if (color_sensor.color == 5): #código para vermelho no ev3
        steering_drive.off()
        tempo = time.time()
        steering_drive.on_for_seconds(steering = 0, speed = -100, seconds = 1)
        steering_drive.on_for_seconds(steering = 100, speed = 70, seconds = 1)
        
main()
