import sys
import threading
from PWMServoControl import *
from time import sleep
# import ActionGroupControl as AGC

servo = PWMServo()

servo.setThreshold(2,1000,1800)
servo.setThreshold(6,1000,1800)

servo.setThreshold(4,1000,1800)
servo.setThreshold(8,1000,1800)


def getServoPulse(id):
    return servo.servo_pwm_duty_now[id]

def getServoDeviation(id):
    return servo.getDeviation(id)

def setServoPulse(id, pulse, use_time):
    servo.setPulse(id, pulse, use_time)

def setServoDeviation(id ,dev):
    servo.setDeviation(id, dev)
    
def saveServoDeviation(id):
    servo.saveDeviation(id)

def unloadServo(id):
    servo.unload(id)

def updatePulse(id):
    servo.updatePulse(id)

def forward(servo_angle=[40, 40, -40, -40] , sleepTime=1.0, servo_rate=[1.0, 1.0]):
    setServoPulse(2, servo_rate[0]*servo_angle[0]*6.25+1500, 250)
    setServoPulse(4, servo_rate[1]*servo_angle[1]*6.25+1500, 250)
    setServoPulse(6, servo_rate[0]*servo_angle[2]*6.25+1500, 250)
    setServoPulse(8, servo_rate[1]*servo_angle[3]*6.25+1500, 250)
    sleep(sleepTime)
# def runActionGroup(num):
#     threading.Thread(target=AGC.runAction, args=(num, )).start()    

# def stopActionGroup():    
#     AGC.stop_action_group() 
#  


SERVO_MIDDLE_VALUE = 1500

if __name__ == "__main__":
    pass