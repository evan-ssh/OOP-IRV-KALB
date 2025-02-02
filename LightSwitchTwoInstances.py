class LightSwitch():
    def __init__(self):
        self.SwitchIsOn = False
    
    def turnON(self):
        self.SwitchIsOn = True

    def turnOFF(self):
        self.SwitchIsOn = False
    
    def showSwitchState(self):
        print(f"The switch is on {self.SwitchIsOn}")