# output
# traffic light 1, 2, 3 & 4

# input
# Walker button 1, 2, 3 & 4
# Sensor 1, 2, 3 & 4

# errors
# one faulty sensor (shows there is a car when there is not, should eventually turn the lights yellow)
# one faulty traffic light (lights should show yellow)

# other notices
# when the trafficlight is red the walksers can cross the road

# trafficlight x and walkerButton x are the same so if walker presses the button 
# the light needs to turn red in order to get the person walk across the road

# when the sensor has signaled a car in the direction of green light, 
# the car is so close it cannot stop to the lights


##       |
##       |                                   |
##       | trafficLight0 ->   trafficLight 1 v
##  -----+------
##       | trafficLigt 2 <-   trafficLight 3 ^
##       |                                   |
##       |
##

## lights 0 and 2 can be green on the same time
## light 1 and 3 can be green on the same time

import numpy as np

#input
def sensorDetection(detectCar):
    if detectCar == True:
        return 20
    return 

def walkerButton(walkerButton):
    if walkerButton == True:
        return 10
    return

# output

def trafficLightChange(lightGreen, lightRed):
    
    if lightGreen == True:
        lightGreen = False
        lightRed = True
    else:
        lightGreen = True
        lightRed = False

    return lightGreen, lightRed

## carDetection from direction 0 and/or 2 and walker from direction 1 and/or 3
## carDetection from direction 1 and/or 3 and walker from direction 0 and/or 2

## carDetection from direction 0 and 1, 0 and 3, 2 and 1 or 2 and 3, no walker
 
## carDetection from direction 0 and/or 2 and walker from direction 0 and/or 2
## carDetection from direction 1 and/or 3 and walker from direction 1 and/or 3

## walkerButton from direction 0 and 1, 0 and 3, 2 and 1 or 2 and 3, no car

## carDetection from direction 0, 1 and 2 or 1, 2 and 3 or 2, 3 and 0 or 3, 0 and 1 or all directions

## walkerButton from direction 0, 1 and 2 or 1, 2 and 3 or 2, 3 and 0 or 3, 0 and 1 or all directions

## carDetection from direction 0, 1 and 2 or 1, 2 and 3 or 2, 3 and 0 or 3, 0 and 1 or all directions as well as
## walkerButton from direction 0, 1 and 2 or 1, 2 and 3 or 2, 3 and 0 or 3, 0 and 1 or all directions


def detection(detection):
    #print(detection)
    if(detection[0] and detection[2] and detection[1] and detection[3]):
        print("detected all directions")
        return 1
        
    elif(detection[0] and detection[1] and detection[2] or detection [1] and detection[2] and detection[3] or detection[2] and detection [3] and detection[0] or detection[3] and detection [0] and detection[1]):
        print("detection from three directions")
        return 2

    elif(detection[0] and detection[1] or detection[1] and detection [2] or detection[2] and detection [3] or detection[3] and detection [0]):
        print("detected from two directions collision")
        return 3

    elif(detection[0] and detection[2] or detection[1] and detection[3]):
        print("detected two directions no collision")
        return 4

    elif(detection[0] or detection[1] or detection[2] or detection[3]):
        print("only one detected")
        return 5

    else:
        print("no detection")
        return 6
    

    

def mainDecisionMaker():
     
    lightGreen =  [False] * 4
    lightRed = [True] * 4
    lightYellow = [False] * 4
    

    length = 8

    
    randTable = np.random.randint(0, 2, size=(length,8))
    
    for i in range(length):
        walkerButton = [False] * 4
        detectCar = [False] * 4
        for j in range (8):
            
            if (randTable[i][j] == 1 and j<4):
                detectCar[j] = True
            elif (randTable[i][j] == 1 and j>3):
                walkerButton[j-4] = True 
        

        scenarioCar = detection(detectCar)
        scenarioWalker = detection(walkerButton)
        

    


    #elif(detectCar[0] & detectCar [2] & (walkerButton[1] | walkerButton[3]) | detectCar[1] & detectCar[3] & (walkerButton[0] | walkerButton[2])):
    #    print("car and walker detected no collision")

    #elif(detectCar[0] & detectCar [2] & (walkerButton[0] | walkerButton[2]) | detectCar[1] & detectCar[3] & (walkerButton[1] | walkerButton[3])):
    #    print("car detected collides with walker")
    

    #print(detectCar)


    

    
    exit


mainDecisionMaker()