#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
en1 = 25

in3 =27
in4 = 17
en2 = 22

temp1=1
speed=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(en1,500)
p2=GPIO.PWM(en2,1000)
p.start(25)
p2.start(25)
print("\n")
print("The default speed & direction of motors is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit tr-turn right tl-turn left")
print("\n")    

def move():
    # Starts a new node
    rospy.init_node('astromech_teleop', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    rate = rospy.Rate(10) #10hz

    
    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):



         vel_msg.linear.x = speed
         vel_msg.linear.y = 0
         vel_msg.linear.z = 0
         vel_msg.angular.x = 0
         vel_msg.angular.y = 0
         vel_msg.angular.z = 0
         velocity_publisher.publish(vel_msg)
	 rospy.sleep(1)
    
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:

         vel_msg.linear.x = -speed
         vel_msg.linear.y = 0
         vel_msg.linear.z = 0
         vel_msg.angular.x = 0
         vel_msg.angular.y = 0
         vel_msg.angular.z = 0
         velocity_publisher.publish(vel_msg)
	 rospy.sleep(1)
            
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':


        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
	rospy.sleep(1)
    
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':

        vel_msg.linear.x = speed
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
	rospy.sleep(1)


        
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':

        vel_msg.linear.x = -2.7
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
	rospy.sleep(1)
        
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='tr':


        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = (speed)/2
        velocity_publisher.publish(vel_msg)
	rospy.sleep(1)

        
        print("turn right")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='tl':

        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = (-speed)/2
        velocity_publisher.publish(vel_msg)
	rospy.sleep(1)

        
        print("turn left")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        x='z'

    elif x=='l':
        speed==1
        print("low")
        p.ChangeDutyCycle(15)
        p2.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        speed=2
        print("medium")
        p.ChangeDutyCycle(40)
        p2.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        speed=2.5
        print("high")
        p.ChangeDutyCycle(55)
        p2.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        #break
    
    else:
        print("<<<  wrong data  >>>")
    print("please enter the defined data to continue.....")



if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
