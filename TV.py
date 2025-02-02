class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        #Default list of channels
        self.channelList = [2,4,5,7,9,11,20,36,44,54,65]
        self.nChannels = len(self.channelList)
        self.ChannelIndex = 0
        self.VOLUME_MINIUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM//2

    def power(self):
        self.isOn = not self.isOn
    


    def volumeUP(self):
        if not self.isOn:
            return

        if self.isMuted:
            self.isMuted = False
            return
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return

        if self.isMuted:
            self.isMuted = False
            return
        if self.volume > self.VOLUME_MAXIMUM:
            self.volume += 1
    def channelUP(self):
        if not self.isOn:
            return
        self.ChannelIndex += 1
        if self.ChannelIndex > self.nChannels:
            self.ChannelIndex = 0 #Return to first channel
    def channelDOWN(self):
        if not self.isOn:
            return
        self.ChannelIndex -= 1
        if self.ChannelIndex < 0:
            self.ChannelIndex = self.nChannels - 1 #Go to top channel
    
    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
    def setChannel(self,channel):
        if channel in  self.channelList:
            self.ChannelIndex = self.channelList.index(channel)
        
    def showInfo(self):
        print("TV STATUS")
        if self.isOn:
            print("The TV is on")
            print(f"Channel is {self.channelList[self.ChannelIndex]}")
            if self.isMuted:
                print("The TV is muted")
            else:
                print(f"Volume is {self.volume}")
        else:
            print("The TV is off")
if __name__ == "__main__":
    tv = TV()
    #Turn the TV on and show status
    tv.power()
    tv.showInfo()
    
    #Change channel up twice, volume up twice, show status
    tv.channelUP()
    tv.channelUP()
    tv.volumeUP()
    tv.volumeUP()
    tv.showInfo()


    #Turn the tv off, show status, turn on, show status
    tv.power()
    tv.showInfo()
    tv.power()
    tv.showInfo()

    #Lower the volume, mute sound, show status
    tv.volumeDown()
    tv.mute()
    tv.showInfo()

    #Change the channel to 11, mute sound, show status
    tv.setChannel(11)
    tv.mute()
    tv.showInfo()
