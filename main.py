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

def trafficLightChange(lightGreen, lightRed, carDirection, case):
    
    if case == 0:
        if(lightRed[0] == False):
            lightGreen[0] = lightRed[0] = False
            lightGreen[2] = lightRed[2] = False
            
        elif(lightRed[1] == False):
            lightGreen[1] = lightRed[1] = False
            lightGreen[3] = lightRed[3] = False

    elif case == 1:
        #it is known that the direction is red
        if carDirection == 0:
            if (lightGreen[1] == True):
                lightGreen[1] = lightRed[1] = False
                lightGreen[3] = lightRed[3] = False
                lightGreen[0] = lightRed[3] = True
                lightGreen[2] = lightRed[2] = True
            else:
                lightGreen[0] = lightRed[0] = True
                lightGreen[2] = lightRed[2] = True
            
        elif carDirection == 3:
            if (lightGreen[2] == True):
                lightGreen[2] = lightRed[2] = False
                lightGreen[0] = lightRed[0] = False
                lightGreen[1] = lightRed[1] = True
                lightGreen[3] = lightRed[3] = True
            else:
                lightGreen[1] = lightRed[1] = True
                lightGreen[3] = lightRed[3] = True

        else:
            if (lightGreen[carDirection-1] == True):
                lightGreen[carDirection-1] = lightRed[carDirection-1] = False #0 #1
                lightGreen[carDirection+1] = lightRed[carDirection+1] = False #2 #3

                if(carDirection == 1):
                    lightGreen[1] = lightRed[1] = True
                    lightGreen[3] = lightRed[3] = True
                else:
                    lightGreen[2] = lightRed[2] = False
                    lightGreen[0] = lightRed[0] = False 



    return lightGreen, lightRed


def detection(detection):
    #print(detection)
    if(detection[0] and detection[2] and detection[1] and detection[3]):
        #print("detected all directions")
        return 1
        
    elif(detection[0] and detection[1] and detection[2] or detection [1] and detection[2] and detection[3] or detection[2] and detection [3] and detection[0] or detection[3] and detection [0] and detection[1]):
        #print("detection from three directions")
        return 2

    elif(detection[0] and detection[1] or detection[1] and detection [2] or detection[2] and detection [3] or detection[3] and detection [0]):
        #print("detected from two directions collision")
        return 3

    elif(detection[0] and detection[2] or detection[1] and detection[3]):
        #print("detected two directions no collision")
        return 4

    elif(detection[0] or detection[1] or detection[2] or detection[3]):
        #print("only one detected")
        return 5

    else:
        #print("no detection")
        return 6
        

def mainDecisionMaker():
     
    lightGreen =  [False] * 4
    lightRed = [True] * 4
    lightYellow = [False] * 4
    
    length = 20
    
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
        
        if (scenarioCar == 6 and scenarioWalker == 1):
            print("change all car lights to red")
            lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, -1, 0)

            print(lightGreen, lightRed)
            
        elif ((scenarioCar == 4 or scenarioCar == 5) and (scenarioWalker == 6 or scenarioWalker == 5 or scenarioWalker == 4)):
            print("one car or parallel cars detected with no walkers, one walker or two parallel walkers")

            if(scenarioWalker == 6):
                print("no walkers, change light to green")
                carDirection = detectCar.index(True)
                if (lightGreen[carDirection] == True):
                    print("already green")
                else: 
                    print("now red, changing direction " + str(carDirection) + " to green")
                    lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, carDirection, 1)
                    
                print(lightGreen, lightRed)

            elif(((detectCar[0] == True or detectCar[2] == True) and (walkerButton[1]== True or walkerButton[3] == True)) or
                 ((detectCar[1] == True or detectCar[3] == True) and (walkerButton[0]== True or walkerButton[2] == True))):
                print("walkers and cars in parrallel")

            else:
                print("walkers and cars in conflict")


        else:
            print("Complex result")


    

    
    exit


mainDecisionMaker()