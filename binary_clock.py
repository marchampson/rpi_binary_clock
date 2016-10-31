# Matrix of all numbers 1-59 in binary and their respective GPIO pins
# Start with HH:MM 12hour version
# Requires 10 LEDs 6 in any one row
# HOURS
# GPIO 1-4
# 0 & 1 = GPIO 1
# 2 = GPIO 2
# 4 = GPIO 3
# 8 = GPIO 4
# numpy 1:
# 11 O'Clock = 1011 = GPIO(1,HIGH) GPIO(2,HIGH) GPIO(3,LOW) GPIO(4,HIGH)

# Current output is correct, need to add to global array and then simply
# list out the GPIO switches increasing the index by 1 (unless Pi GPIOs
# start at 0?
#import Rpi.GPIO as GPIO
import time
import numpy as np
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

now = time.localtime()
#print(now.tm_hour)
hour = now.tm_hour
if(hour > 12):
    hour = hour - 12

def bin_time(num_time_elements):
    time_array = []
    for i in range(0, num_time_elements):
        bin = [int(x) for x in list('{0:0b}'.format(i))]
        time_array.append(bin)

    return time_array

def set_gpio_pins(time_group, group_elements, padding = 6):
    t = group_elements[time_group]
    t_elements = len(t)

    # Set the padding LEDs to OFF
    pad = padding - t_elements
    for i in range(0,pad):
        print("GPIO {} OFF".format(i + 1))

    # Set the remaining pins to I/O
    for i in range(0, t_elements):
        if (group_elements[time_group][i] == 0):
            print("GPIO {} OFF".format(i + pad + 1))
        else:
            print("GPIO {} ON".format(i + pad + 1))

# Display time groups for sanity checking
hours = bin_time(13)
print(hours[hour])

minutes = bin_time(60)
print(minutes[now.tm_min])

seconds = bin_time(60)
print(seconds[now.tm_sec])

h = hours[hour]
hour_elements = len(h)

# Set GPIO pins
set_gpio_pins(hour, hours, 6)
set_gpio_pins(now.tm_min, minutes, 6)
set_gpio_pins(now.tm_sec, seconds, 6)
