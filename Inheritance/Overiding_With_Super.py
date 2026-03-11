class Vehicle:
    def start(self):
        print("Starting...")

class Car(Vehicle):
    def start(self):
        print('Push Starting the Car....')
        super().start()

defender=Car()
defender.start()