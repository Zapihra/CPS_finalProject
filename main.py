import numpy as np
import matplotlib.pyplot as plt

# output
def trafficLightChange(lightGreen, lightRed, carDirection, case):
    
    if case == 0:
       
        lightGreen[0] = lightGreen[1] = False
        lightGreen[2] = lightGreen[3] = False
        
        lightRed[0] = lightRed[1] = True
        lightRed[2] = lightRed[3] = True

    elif case == 1:
        #it is known that the direction is red
        if carDirection == 0 or carDirection == 2:
            
            lightGreen[1] = lightRed[0] = False
            lightGreen[3] = lightRed[2] = False
            lightGreen[0] = lightRed[1] = True
            lightGreen[2] = lightRed[3] = True
            
        else:
            lightGreen[2] = lightRed[3] = False
            lightGreen[0] = lightRed[1] = False
            lightGreen[1] = lightRed[0] = True
            lightGreen[3] = lightRed[2] = True
    
    elif case == 2:
        
        if lightGreen[0] == True:
            lightGreen[2] = lightRed[3] = False
            lightGreen[0] = lightRed[1] = False
            lightGreen[1] = lightRed[0] = True
            lightGreen[3] = lightRed[2] = True
        else:
            lightGreen[1] = lightRed[0] = False
            lightGreen[3] = lightRed[2] = False
            lightGreen[0] = lightRed[1] = True
            lightGreen[2] = lightRed[3] = True

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
     
    lightGreen =  [False, True] * 2
    lightRed = [True, False] * 2
    lightYellow = [False] * 4
    faultDetection = 0
    faultDetectionList = []
    length = 1000
    
    #input of 4 sensors and 4 walker buttons for the length of 8
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

        if detectCar[0] == True:
            faultDetection = faultDetection + 1
        else:
            faultDetection = 0

        faultDetectionList.append(faultDetection)
        
        if faultDetection >= 13:
            print(faultDetection)

        
        if (scenarioCar == 6 and scenarioWalker == 6):
            #print("no cars, no walkers, no need to change anything")
            continue

        elif (scenarioCar == 6):   
            #print("change all car lights to red")
            lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, -1, 0)

        elif ((scenarioCar == 4 or scenarioCar == 5) and (scenarioWalker == 6 or scenarioWalker == 5 or scenarioWalker == 4)):
            #print("one car or parallel cars detected with no walkers, one walker or two parallel walkers")
            
            #print(detectCar, walkerButton)
            carDirection = detectCar.index(True)
            
            if(scenarioWalker == 6):
                #print("no walkers, change light to green")
                
                if (lightGreen[carDirection] == True):
                    #print("already green")
                    continue
                else: 
                    #print("now red, changing direction " + str(carDirection) + " to green")
                    lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, carDirection, 1)

            elif(((detectCar[0] == True or detectCar[2] == True) and (walkerButton[1]== True or walkerButton[3] == True)) or
                 ((detectCar[1] == True or detectCar[3] == True) and (walkerButton[0]== True or walkerButton[2] == True))):
                #print("walkers and cars in parrallel")
                if(lightGreen[carDirection] == True):
                    #print("already green")
                    continue
                else: 
                    #print("now red, changing direction " + str(carDirection) + " to green")
                    lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, carDirection, 1)

            else:
                #print("walkers and cars in conflict")

                if (lightGreen[0] == False and lightGreen[1] == False):
                    #print("all lights were red")
                    lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, carDirection, 1)
                    
                #print("waiting for walkers or cars and then changing lights")
                lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, carDirection, 2)

        else:
            #print("walkers and cars in multiple direction")
            carDirection = detectCar.index(True)
            
            if (lightGreen[0] == False and lightGreen[1] == False):
                #print("all lights were red")
                lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, carDirection, 1)
                
            #print("waiting for walkers or cars and then changing lights")
            lightGreen, lightRed = trafficLightChange(lightGreen, lightRed, carDirection, 2)
    
    #print(faultDetectionList)

    plt.figure(figsize=(15,8))
    plt.plot(faultDetectionList)
    plt.xlabel("Time")
    plt.ylabel("Sensor0 detections of cars in a row")
    plt.grid(True)
    plt.show()

    
    return 0


mainDecisionMaker()