class TV:
    def __init__(self):
        self.is_on = False
    def turnOn(self):
        self.is_on = True
    def turnOff(self):
        self.is_on  = False
    def showStatus(self):
        if self.is_on == True:
            print("TV is on")
        else:
            print("TV is off")
set1 = TV()

set1.turnOn()
set1.showStatus
