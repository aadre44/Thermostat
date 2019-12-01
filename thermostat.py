#import RPi.GPIO as GPIO
import time
from weatherAPI import weatherInfo

rpiMode = False
if(rpiMode):
    GPIO.setmode(GPIO.BOARD)

class thermo():
    """ SETUP
    3 relays ( fan, ac, heat) pins
    """
    fanPin = 29
    acPin = 31
    heatPin = 33

    # GPIO SETUP
    """
    GPIO.setup(fanPin, GPIO.OUT)
    GPIO.setup(acPin, GPIO.OUT)
    GPIO.setup(furnacePin, GPIO.OUT)
    """
    #Global variables
    ac = False
    heat = False
    auto = False
    autoSet = False
    off = False

    desiredTemp = 80
    currentTemp = 5

    weather = weatherInfo()

    """
    Funcitons
    """

    def tempUp(self):
        if (self.desiredTemp == 99):
            self.desiredTemp = 0
        self.desiredTemp+= 1
        print("desired "+str(self.desiredTemp))

    def tempDown(self):
        if (self.desiredTemp == 0):
            self.desiredTemp = 99
        self.desiredTemp-= 1
        print("desired "+str(self.desiredTemp))

    def turnOff(self):
        self.off = True
        print("EVERYTHING OFF")

    def acOn(self):
        if (self.ac == False):
            self.ac = True
            #print("AC ON")
            self.heat = False
           # print("Heat OFF")
        else:
            self.ac = False
            #print("AC OFF")


    def heatOn(self):
        if (self.heat == False):
            self.heat = True
            #print("Heat ON")
            self.ac = False
            #print("AC OFF")
        else:
            self.heat = False
            #print("Heat OFF")

    def autoOn(self):
        if( self.auto == False):
            self.auto = True
            print("Auto On")
        else:
            self.auto = False
            print("Auto off")

    def getDesiredTemp(self):
        print("Here is the current temp "+str(self.desiredTemp))
        return self.desiredTemp

    def getCurTemp(self):
        print("Here is the current temp "+str(self.currentTemp))
        return self.currentTemp

    """
    runs a infinite loop that checks the control bool values every iteration and adjust the thermostats function accordingly
    """
    def cycle(self):
        print("RUNNING CYCLE")
        while True:
            #self.getCommand()
            if(self.ac):
                self.turnHeatOff()
                self.turnAcOn()
            elif (self.heat):
                self.turnAcOff()
                self.turnHeatOn()

            elif (self.off):
                self.turnAcOff()
                self.turnHeatOff()

            if (self.auto):
                print("autoSet value: "+str(self.autoSet))
                if(self.autoSet):
                    self.checkAutoTemp()
                else:
                    self.turnAutoOn()
            elif(self.autoSet):
                self.turnAutoOff()

            self.makeSureOffisOff()


    def getAuto(self):
        return self.auto

    """
    Sets the ac bool to false and the ac gpio pin to low
    """
    def turnAcOff(self):
        # GPIO.output(acPin, GPIO.LOW)
        self.ac = False

    """
    Sets the ac bool to false and the ac gpio pin to high
    """
    def turnAcOn(self):
        # GPIO.output(acPin, GPIO.HIGH)
        self.ac = True
        print("ac successfully turned on")

    """
    Sets the heat bool to false and the heat gpio pin to low
    """
    def turnHeatOff(self):
        # GPIO.output(heatPin, GPIO.LOW)
        self.heat = False
        print("heat successfully turned off")

    """
    Sets the heat bool to false and the heat gpio pin to high
    """
    def turnHeatOn(self):
        # GPIO.output(heatPin, GPIO.HIGH)
        self.heat = True
        print("heat successfully turned on")

    """
    Sets the autoSet bool to false and the fan gpio pin to low
    """
    def turnAutoOff(self):
        # GPIO.output(fanPin, GPIO.LOW)
        self.autoSet = False
        print("Auto successfully turned off")

    """
    Sets the autoSet bool to true and the fan gpio pin to high
    """
    def turnAutoOn(self):
        # GPIO.output(fanPin, GPIO.HIGH)
        self.autoSet = True
        print("AutoSET successfully turned on")
        print("autoSet value2: " + str(self.autoSet))

    """
    Checks the current temp and turns the fan gpio pin on or off depending on which control bool is on and 
    if the values of the current and desired temp
    """
    def checkAutoTemp(self):
        if(self.ac and self.auto):
            if (self.desiredTemp <= self.currentTemp):
                # GPIO.output(fanPin, GPIO.LOW)
                print("TEMP is reached fan turned off")
            else:
                # GPIO.output(fanPin, GPIO.HIGH))
                print("TEMP is not reached fan turned on")
        elif(self.heat == True and self.auto):
            if (self.desiredTemp <= self.currentTemp):
                # GPIO.output(fanPin, GPIO.LOW)
                print("TEMP is reached fan turned off")
            else:
                # GPIO.output(fanPin, GPIO.HIGH))
                print("TEMP is not reached fan turned on")
        else:
            print("nothing to see here")

    """
    Asks user for commands that will control the thermostat when ui is not used
    """
    def getCommand(self):
        command = input("what do you want to do sir? \n")

        if(command == "ac"):
            self.acOn()
        elif(command == "heat"):
            self.heatOn()
        elif (command == "off"):
            self.turnOff()
        elif (command == "auto"):
            self.autoOn()

    """
    Makes sure that if a control bool was set to false between cycles the gpio pin is set to low
    """
    def makeSureOffisOff(self):
        if(self.ac == False):
            # GPIO.output(acPin, GPIO.LOW)
            print("making sure ac is off")
        if (self.heat == False):
            # GPIO.output(heatPin, GPIO.LOW)
            print("making sure heat is off")