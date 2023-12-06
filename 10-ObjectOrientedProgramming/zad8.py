class Phone():
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.apps = []
        self.memory = memory
    def charge(self,battery):
        if battery >= 100:
            battery = 100
            self.current_battery = battery
        else:
            self.current_battery = battery
    def downloadApp(self, app):
        self.apps.append(app)

phone = Phone ("Iphone 6", "6'", '64 GB')

phone.charge(78)
phone.downloadApp("pinterest")
phone.charge(130)
print(phone.current_battery, phone.apps)