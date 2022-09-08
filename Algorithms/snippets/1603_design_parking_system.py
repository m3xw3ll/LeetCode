class ParkingSystem:
    def __init__(self, big, medium, small):
        self.space = {
            1: big,
            2: medium,
            3: small
        }

    def add_car(self, car_type):
        if self.space[car_type]:
            self.space[car_type] -= 1
            return True
        return False

obj = ParkingSystem(1, 1, 0)
param_1 = obj.add_car(1)
param_2 = obj.add_car(2)
param_3 = obj.add_car(3)
print(param_1, param_2, param_3)