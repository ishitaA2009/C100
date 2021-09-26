class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.model = model
        self.speed_limit = speed_limit
        
    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelarate(self):    
        print("Accelarating")

    def change_gear(self,gear_type):
        print("gear_changed")

audi = Car("A6","red","audi","80")
print(audi.color)
print(audi.model)                    
