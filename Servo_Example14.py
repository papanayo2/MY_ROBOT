#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm2 = PWM(0x41)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

up = 300#230
down = 400#470

sg90min = 300#150 # 0 degrees - right
sg90max = 500#650 # 180 degrees - left

mg995fmin = 300#150
mg995fmax = 500#600

mg995rmin = 300#200
mg995rmax = 500#620

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)
pwm2.setPWMFreq(60)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(0, 0, mg995fmin)
  pwm.setPWM(1, 0, mg995fmin)
  pwm.setPWM(2, 0, mg995fmin)
  pwm.setPWM(3, 0, mg995fmin)

  time.sleep(1)

  pwm.setPWM(4, 0, mg995rmin)
  pwm.setPWM(5, 0, mg995rmin)
  pwm.setPWM(6, 0, mg995rmin)
  pwm.setPWM(7, 0, mg995rmin)

  time.sleep(1)

  pwm.setPWM(8, 0, mg995fmin)
  pwm.setPWM(9, 0, mg995fmin)
  pwm.setPWM(10, 0, mg995fmin)

  time.sleep(1)

  pwm.setPWM(12, 0, sg90min)
  pwm.setPWM(13, 0, sg90min)
  pwm.setPWM(14, 0, sg90min)
  pwm.setPWM(15, 0, sg90min)

  time.sleep(1)

  #--------------------------

  pwm2.setPWM(0, 0, mg995fmin)
  pwm2.setPWM(1, 0, mg995fmin)
  pwm2.setPWM(2, 0, mg995fmin)
  pwm2.setPWM(3, 0, mg995fmin)

  time.sleep(1)

  pwm2.setPWM(4, 0, mg995fmin)
  pwm2.setPWM(5, 0, mg995fmin)
  pwm2.setPWM(6, 0, mg995fmin)
  pwm2.setPWM(7, 0, mg995fmin)

  time.sleep(1)

  pwm2.setPWM(8, 0, mg995fmin)
  pwm2.setPWM(9, 0, mg995fmin)
  pwm2.setPWM(10, 0, mg995fmin)

  time.sleep(1)

  pwm2.setPWM(12, 0, sg90min) # camera mount base
  pwm2.setPWM(13, 0, down) # camera mount upper part


  time.sleep(2)

  pwm.setPWM(0, 0, mg995fmax)
  pwm.setPWM(1, 0, mg995fmax)
  pwm.setPWM(2, 0, mg995fmax)
  pwm.setPWM(3, 0, mg995fmax)

  time.sleep(1)

  pwm.setPWM(4, 0, mg995rmax)
  pwm.setPWM(5, 0, mg995rmax)
  pwm.setPWM(6, 0, mg995rmax)
  pwm.setPWM(7, 0, mg995rmax)

  time.sleep(1)

  pwm.setPWM(8, 0, mg995fmax)
  pwm.setPWM(9, 0, mg995fmax)
  pwm.setPWM(10, 0, mg995fmax)

  time.sleep(1)

  pwm.setPWM(12, 0, sg90max)
  pwm.setPWM(13, 0, sg90max)
  pwm.setPWM(14, 0, sg90max)
  pwm.setPWM(15, 0, sg90max)

  time.sleep(1)

#--------------------------

  pwm2.setPWM(0, 0, mg995fmax)
  pwm2.setPWM(1, 0, mg995fmax)
  pwm2.setPWM(2, 0, mg995fmax)
  pwm2.setPWM(3, 0, mg995fmax)

  time.sleep(1)

  pwm2.setPWM(4, 0, mg995fmax)
  pwm2.setPWM(5, 0, mg995fmax)
  pwm2.setPWM(6, 0, mg995fmax)
  pwm2.setPWM(7, 0, mg995fmax)

  time.sleep(1)

  pwm2.setPWM(8, 0, mg995fmax)
  pwm2.setPWM(9, 0, mg995fmax)
  pwm2.setPWM(10, 0, mg995fmax)

  time.sleep(1)

  pwm2.setPWM(12, 0, sg90max) # camera mount base
  pwm2.setPWM(13, 0, up) # camera mount upper part

  time.sleep(2)


