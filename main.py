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

def mainDecisionMaker():
     
    lightGreen =  [False] * 4
    lightRed = [True] * 4
    lightYellow = [False] * 4
    walkerButton = [False] * 4
    detectCar = [False] * 4

    table = [True, False, False, True, False, False, True, False]
    i = 0
    for i in range(4): 
        detectCar[i] = table[i]
        walkerButton[i] = table[i+4]
    
    

    print(detectCar, walkerButton)


    

    
    exit


mainDecisionMaker()