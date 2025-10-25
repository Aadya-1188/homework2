class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        final_fare = total_fare + (0.1 * total_fare)
        return final_fare


bus = Bus(50)
print("Total Bus fare:", int(bus.fare()))
