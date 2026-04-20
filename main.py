# output
# traffic light 1, 2, 3 & 4

# input
# Walker button 1, 2, 3 & 4
# Sensor 1, 2, 3 & 4

# errors
# one faulty sensor (shows there is a car when there is not, should eventually turn the lights yellow)
# one faulty traffic light (lights should show yellow)

#inputs
def sensor1(detectCar):
    if detectCar == True:
        return 20
    
    if detectCar == False:
        return 0

    return 0

def sensor2(detectCar):
    if detectCar == True:
        return 20
    
    if detectCar == False:
        return 0
    return 0

def sensor3(detectCar):
    if detectCar == True:
        return 20
    
    if detectCar == False:
        return 0

    return 0

def sensor4(detectCar):
    if detectCar == True:
        return 20
    
    if detectCar == False:
        return 0

    return 0

def walkerButton(walkerButton):
    if walkerButton == True:
        return 10
    return


# outputs

def trafficLightChange(lightGreen, lightRed):
    
    if lightGreen == True:
        lightGreen = False
        lightRed = True
    else:
        lightGreen = True
        lightRed = False

    return lightGreen, lightRed

def mainDecisionMaker():
     
    lightGreen1 = lightGreen2 = lightGreen3 = lightGreen4 = False
    lightRed1 = lightRed2 = lightRed3 = lightRed4 = True
    lightYellow1 = lightYellow2 = lightYellow3 = lightYellow4 = False
    walkerButton1 = walkerButton2 = walkerButton3 = walkerButton4 = False


    table = [True, False, False, True, False, False, True, False]
    waitTime1 = sensor1(table[0])
    waitTime2 = sensor2(table[1])

    print(lightGreen1, lightRed1)
    
    lightGreen1, lightRed1 = trafficLightChange(lightGreen1, lightRed1)
    print(lightGreen1, lightRed1)

    
    exit


mainDecisionMaker()