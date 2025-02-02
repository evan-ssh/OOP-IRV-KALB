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
        