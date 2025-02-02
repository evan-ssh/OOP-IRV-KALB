class DimmerSwitch():
    def __init__(self):
        self.SwitchIsOn = False
        self.brightness = 0
    
    def turnON(self):
        self.SwitchIsOn = True

    def turnOFF(self):
        self.SwitchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1
            
        
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1
    
    def showSwitchState(self):
        print(f"The switch is on {self.SwitchIsOn}")
        print(f"The brightness level is {self.brightness}")