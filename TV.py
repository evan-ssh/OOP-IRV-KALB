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