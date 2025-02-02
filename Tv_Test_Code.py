from TV import TV
#Import the TV class from TV.py Saves Space In The Main File
while True:
    tv = TV()
    #Turn the TV on and show status
    tv.power()
    tv.showInfo()
    print()
    #Change channel up twice, volume up twice, show status
    tv.channelUP()
    tv.channelUP()
    tv.volumeUP()
    tv.volumeUP()
    tv.showInfo()
    print()
    #Turn the tv off, show status, turn on, show status
    tv.power()
    tv.showInfo()
    tv.power()
    tv.showInfo()
    print()
    #Lower the volume, mute sound, show status
    tv.volumeDown()
    tv.mute()
    tv.showInfo()
    print()
    #Change the channel to 11, mute sound, show status
    tv.setChannel(11)
    tv.mute()
    tv.showInfo()
    break
