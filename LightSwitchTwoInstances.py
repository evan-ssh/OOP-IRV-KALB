class LightSwitch():
    def __init__(self):
        self.SwitchIsOn = False
    
    def turnON(self):
        self.SwitchIsOn = True

    def turnOFF(self):
        self.SwitchIsOn = False
    
    def showSwitchState(self):
        print(f"The switch is on {self.SwitchIsOn}")
    
if __name__ == "__main__":
    light1 = LightSwitch()
    light2 = LightSwitch()
    light1.showSwitchState()
    light2.showSwitchState()
    light1.turnON()
    light2.turnON()
    light1.showSwitchState()
    light2.showSwitchState()
    light1.turnOFF()
    light2.turnOFF()
    light1.showSwitchState()
    light2.showSwitchState()