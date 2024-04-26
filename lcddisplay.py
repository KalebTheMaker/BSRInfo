from subprocess import run

class LCDDisplay():
    def __init__(self, path):
        self.path = path

    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path
    
    def powerOff(self):
        print("Shutting down power")
        with open(self.path, "w") as bl_file:
            bl_file.write("1")

    def powerOn(self):
        print("Turning on Power")
        with open(self.path, "w") as bl_file:
            bl_file.write("0")

####################################################################
# CLASS TESTING BELOW
####################################################################
# import time
# lcd = LCDDisplay("/sys/class/backlight/soc:backlight/bl_power")

# print(lcd.getPath())
# lcd.powerOff()
# time.sleep(1)
# lcd.powerOn()
